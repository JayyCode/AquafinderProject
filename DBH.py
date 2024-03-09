import mysql.connector
import datetime
from mysql.connector.abstracts import MySQLCursorAbstract


class DatabaseHandler:

    def __init__( self, seller, product_list=None, price_list=None, desc=None, links = list):
        self.links = links
        self.product_list = product_list
        self.price_list = price_list
        self.desc = desc
        self.seller = seller
        tags = self.pull_tags(product_list)

        self.sourceProduct(seller, product_list, price_list, desc, links, tags)


    def pull_tags(self, products):
        self.products = products
        handler = trie()
        listem = []
        holder_tag = ''

        print(products)

        for product in products:
            holder= ''
            temp = []
            temps = product.split()
            for word in temps:
                upper = word.upper()
                temp.append(upper)
                print(temp)

            for words in temp:
                state = handler.is_word(words)
                print(state)
                if state:
                    holder = words
                else:
                    holder = 'NULL'

            listem.append(holder)
            holder = ''

        print(listem)
        return listem

    def sourceProduct(self, seller, products, prices, desc, links, tags):
        self.links = links
        self.seller = seller
        self.tags = tags


        date = datetime.datetime.today()
        date_time= date.strftime('%Y-%m-%d %H:%M:%S')

        seller_url = "https://www." + seller +".com"


        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rw1010419",
            database="aquafinder"
        )
        cursor = connection.cursor()
        data_size = len(products)

        cursor.execute("INSERT IGNORE INTO sellers (SELLER_NAME, SELLER_URL) VALUES (%s, %s)", (seller, seller_url))
        connection.commit()
        print('tags',type(tags[1]))
        print('links',type(links[1]))
        print('desc',type(desc[1]))
        print('prod',type(products[1]))
        print('price',type(prices[1]))
        print('tag',type(tags[1]))


        for i in range (data_size):
            tag = tags[i]
            link = links[i]
            descrip = desc[i]
            product = products[i]
            price = prices[i].replace("$", "")
            tag = tags[i]
            values  = '{0}', '{1}', '{2}', '{3}','{4}','{5}', '{6}'
            try:                                    #0              1      2                  3        4      5         6
                sql1 = ("INSERT  INTO product_feed(PRODUCT_NAME, PRICE, PRODUCT_DESCRIPTION,SELLER,ENTITY,LAST_UPDATE,PRODUCT_URL) "
                        "VALUES ('{0}', '{1}', '{2}', '{3}','{4}','{5}' ,'{6}')").format(product,price,descrip,seller,tag,date_time,link)
                cursor.execute(sql1)
                connection.commit()


            except mysql.connector.errors.IntegrityError as e:
                sql2 = ("UPDATE PRODUCT_FEED "
                        "SET PRICE ='{0}', PRODUCT_DESCRIPTION = '{1}', LAST_UPDATE = '{2}' "
                        "WHERE PRODUCT_NAME = '{3}'".format(price,descrip,date_time,product))
                cursor.execute(sql2)
                connection.commit()


            except mysql.connector.Error as x:
                print("Error in MySQL: ", x)
                connection.rollback()  # Rollback transaction if an error occurs



        print("Products added successfully")
        cursor.close()
        connection.close()





class trie:

    def __init__(self):

        self.root = {'*' : '*'}
        fish_list = [
            "CLOWN",
            "ANGELFISH",
            "BUTTERFLY",
            "BASSELT",
            "SALTWATER",
            "BLENNY",
            "GOBY",
            "DAMSEL",
            "CHROMIS",
            "GROUPER",
            "WRASSE",
            "PUFFER",
            "HAWKFISH",
            "LIONFISH",
            "TANG",
            "SURGEON",
            "RABBITFISH",
            "SEAHORSE",
            "FOXFACE",
            "DOTTYBACK",
            "JAWFISH",
            "CARDINAL",
            "DRAGONET",
            "FILEFISH",
            "PIPEFISH",
            "DARTFISH",
            "GOATFISH",
            "ANTHIAS",
            "BOXFISH",
            "SQUIRRELFISH",
            "SCORPIONFISH",
            "HOGFISH",
            "OTHER SALTWATER VERTABERATE",
            "SNAIL",
            "CRAB",
            "URCHIN",
            "SHRIMP",
            "LOBSTER",
            "POD",
            "CONCH",
            "STARFISH",
            "CLAM",
            "ANEMONE",
            "SLUG",
            "CUCUMBER",
            "FAN WORM",
            "MACROALGA",
            "OTHER CLEANUP CREW AND INVERTEBRATE",
            "CORAL",
            "ACROPORA",
            "MONTIPORA",
            "EUPHILIA",
            "ZOANTHID",
            "MUSHROOM",
            "TETRA",
            "BARB",
            "DANIO",
            "CATFISH",
            "PLATY",
            "GUPPY",
            "SWORDTAIL",
            "MOLLIE",
            "KILLIFISH",
            "BETTA",
            "DISCUS",
            "GOURAMI",
            "RAINBOW FISH",
            "GOLDFISH",
            "RAM",
            "FANCY GOLDFISH",
            "GOLDFISH",
            "KOI",
            "CICHLID",
            "AFRICAN CICHLID",
            "AMERICAN CICHLID",
            "BICHIR",
            "EEL",
            "GUDEON",
            "LOACH",
            "AROWANA",
            "CORYDORAS",
            "OTHER FRESHWATER VERTABERATE",
            "APOSTIGRAMMING",
            "PLANT",
            "OTHER FRESHWATER INVERTEBRATE"
        ]

        for word in fish_list:
            self.add_word(word)

    def add_word(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node['*'] = '*'  # Mark end of the word

    def is_word(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return '*' in current_node

