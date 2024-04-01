import sqlalchemy
from sqlalchemy import URL, create_engine
import datetime


import pandas as pd

# connection_string = 'DRIVER=SQL Server;SERVER=aquafinder.database.windows.net;DATABASE=aquafinder;UID=aquaticshit101;PWD=5plish5plashnigga!;&autocommit=True'
# connection_url = URL.create("mssql+pyodbc", query = {'odbc_connect':connection_string})
# engine = create_engine(connection_url, use_setinputsizes = False, echo = False)

# aquafinder = engine.connect()

# if aquafinder:
#     print('Connection to database was successful')

# Base = declarative_base()

# class Sellers(Base):
#     __tablename__ = 'sellers'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     url = Column(String)

# class ProductFeed(Base):
#     __tablename__ = 'product_feed'

#     id = Column(Integer, primary_key=True)
#     product_name = Column(String)
#     price = Column(String)
#     product_description = Column(String)
#     seller = Column(String)
#     entity = Column(String)
#     last_update = Column(DateTime, default=datetime.datetime.utcnow )
#     product_url = Column(String)



class DatabaseHandler:
 
    def __init__(
        self, seller, product_list=None, price_list=None, desc=None, links=list
    ):
        self.links = links
        self.product_list = product_list
        self.price_list = price_list
        self.desc = desc
        self.seller = seller
        tags = self.pull_tags(product_list)
        aquafinder = self.connection_start()

        self.sourceProduct(aquafinder,seller, product_list, price_list, desc, links, tags)
  
    def connection_start(self):
        connection_string = 'DRIVER=SQL Server;SERVER=aquafinder.database.windows.net;DATABASE=aquafinder;UID=aquaticshit101;PWD=5plish5plashnigga!;&autocommit=True'
        connection_url = URL.create("mssql+pyodbc", query = {'odbc_connect':connection_string})
        engine = create_engine(connection_url, use_setinputsizes = False, echo = False)

        aquafinder_DB = engine.connect()

        if aquafinder_DB:
            print('Connection to database was successful')
            return aquafinder_DB
        else:
            print('Connection Not Established')
        
    def insert_data(self, db_connection ,data, table, replace = False):
        self.table = table 
        try:
            data_frame = pd.DataFrame(data)
        
            if replace:
                existing_df = pd.read_sql('SELECT * FROM aquafinder.{}'.format(table), con=db_connection)
                for column in existing_df:
                    if existing_df[column].is_unique:
                        key=column

                # Merge the new data with the existing DataFrame based on a common key
                merged_df = pd.merge(existing_df, data_frame, on=key, how='outer')

                # Update existing rows with values from the new data
                merged_df.update(merged_df.filter(like='_y'))

                # Write the updated DataFrame back to the database
                merged_df.to_sql('your_table', con=db_connection, if_exists='replace', index=False)
            else:
                data_frame.to_sql(table,con = db_connection, schema='aquafinder', if_exists='append', index=False)
        except ValueError as e:
            data_frame = pd.DataFrame(data, index=[0])
            if replace:
                data_frame.to_sql(table,con = db_connection, schema='aquafinder', if_exists = 'replace', index=False)
            else:
                data_frame.to_sql(table,con = db_connection, schema='aquafinder', if_exists='append', index=False)
            

    def pull_tags(self, products):

        self.products = products
        handler = trie()
        listem = []
        holder_tag = ""

        print(products)

        for product in products:
            holder = ""
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
                    holder = "NULL"

            listem.append(holder)
            holder = ""

        print(listem)
        return listem

   
        self.products = products
        handler = trie()
        listem = []
        holder_tag = ""

        print(products)

        for product in products:
            holder = ""
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
                    holder = "NULL"

            listem.append(holder)
            holder = ""

        print(listem)
        return listem

    def sourceProduct(self, db_connection, seller, products, prices, desc, links, tags):
        self.links = links
        self.seller = seller
        self.tags = tags
        data_size = len(products)
        self.prices = prices
        formatted_price = []
        date = datetime.datetime.today()
        date_time = date.strftime("%Y-%m-%d %H:%M:%S")
        seller_url = "https://www." + seller[0] + ".com"
        for i in range(data_size):
            price = prices[i].replace("$", "")
            formatted_price.append(price)

        seller_data = {'SELLER_NAME':seller[0],
                       'SELLER_URL':seller_url}
   
        product_data = {'PRODUCT_NAME': products,
                        'PRICE': formatted_price,
                        'PRODUCT_DESCRIPTION': desc,
                        'SELLER': seller,
                        'ENTITY': tags,
                        'LAST_UPDATE': date_time,
                        'PRODUCT_URL': links,
                        }
        
        print("tags", type(tags[1]))
        print("links", type(links[1]))
        print("desc", type(desc[1]))
        print("prod", type(products[1]))
        print("price", type(prices[1]))
        print("tag", type(tags[1]))

        self.insert_data(db_connection,seller_data,'sellers', replace=True)

        self.insert_data(db_connection,product_data,'product_feed', replace=True)

        print("Products added successfully")

        # for i in range(data_size):
        #     tag = tags[i]
        #     link = links[i]
        #     descrip = desc[i]
        #     product = products[i]
    #price = prices[i].replace("$", "")
        #     tag = tags[i]
            
class trie:

    def __init__(self):

        self.root = {"*": "*"}
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
            "OTHER FRESHWATER INVERTEBRATE",
        ]

        for word in fish_list:
            self.add_word(word)

    def add_word(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node["*"] = "*"  # Mark end of the word

    def is_word(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return "*" in current_node
