



import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
import pandas as pd

import mysql.connector
import datetime
from mysql.connector.abstracts import MySQLCursorAbstract

connection_string = 'DRIVER=SQL Server;SERVER=aquafinder.database.windows.net;DATABASE=aquafinder;UID=aquaticshit101;PWD=5plish5plashnigga!;&autocommit=True'
connection_url = URL.create("mssql+pyodbc", query = {'odbc_connect':connection_string})
engine = create_engine(connection_url, use_setinputsizes = False, echo = False)

aquafinder = engine.connect()

if aquafinder:
    print("baller")

def querynigga():
    return pd.read_sql('select * from aquafinder.sellers',con=aquafinder)


data = querynigga()

print (data)


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
















# # import datetime


# # date = datetime.datetime.today()
# # print(date)


# # class trie:

# #     def __init__(self):

# #         self.root = {"*": "*"}
# #         fish_list = [
# #             "CLOWN",
# #             "ANGELFISH",
# #             "BUTTERFLY",
# #             "BASSELT",
# #             "SALTWATER",
# #             "BLENNY",
# #             "GOBY",
# #             "DAMSEL",
# #             "CHROMIS",
# #             "GROUPER",
# #             "WRASSE",
# #             "PUFFER",
# #             "HAWKFISH",
# #             "LIONFISH",
# #             "TANG",
# #             "SURGEON",
# #             "RABBITFISH",
# #             "SEAHORSE",
# #             "FOXFACE",
# #             "DOTTYBACK",
# #             "JAWFISH",
# #             "CARDINAL",
# #             "DRAGONET",
# #             "FILEFISH",
# #             "PIPEFISH",
# #             "DARTFISH",
# #             "GOATFISH",
# #             "ANTHIAS",
# #             "BOXFISH",
# #             "SQUIRRELFISH",
# #             "SCORPIONFISH",
# #             "HOGFISH",
# #             "OTHER SALTWATER VERTABERATE",
# #             "SNAIL",
# #             "CRAB",
# #             "URCHIN",
# #             "SHRIMP",
# #             "LOBSTER",
# #             "POD",
# #             "CONCH",
# #             "STARFISH",
# #             "CLAM",
# #             "ANEMONE",
# #             "SLUG",
# #             "CUCUMBER",
# #             "FAN WORM",
# #             "MACROALGA",
# #             "OTHER CLEANUP CREW AND INVERTEBRATE",
# #             "CORAL",
# #             "ACROPORA",
# #             "MONTIPORA",
# #             "EUPHILIA",
# #             "ZOANTHID",
# #             "MUSHROOM",
# #             "TETRA",
# #             "BARB",
# #             "DANIO",
# #             "CATFISH",
# #             "PLATY",
# #             "GUPPY",
# #             "SWORDTAIL",
# #             "MOLLIE",
# #             "KILLIFISH",
# #             "BETTA",
# #             "DISCUS",
# #             "GOURAMI",
# #             "RAINBOW FISH",
# #             "GOLDFISH",
# #             "RAM",
# #             "FANCY GOLDFISH",
# #             "GOLDFISH",
# #             "KOI",
# #             "CICHLID",
# #             "AFRICAN CICHLID",
# #             "AMERICAN CICHLID",
# #             "BICHIR",
# #             "EEL",
# #             "GUDEON",
# #             "LOACH",
# #             "AROWANA",
# #             "CORYDORAS",
# #             "OTHER FRESHWATER VERTABERATE",
# #             "APOSTIGRAMMING",
# #             "PLANT",
# #             "OTHER FRESHWATER INVERTEBRATE",
# #         ]

# #         for word in fish_list:
# #             self.add_word(word)

# #     def add_word(self, word):
# #         current_node = self.root
# #         for char in word:
# #             if char not in current_node:
# #                 current_node[char] = {}
# #             current_node = current_node[char]
# #         current_node["*"] = "*"  # Mark end of the word

# #     def is_word(self, word):
# #         current_node = self.root
# #         for char in word:
# #             if char not in current_node:
# #                 return False
# #             current_node = current_node[char]
# #         return "*" in current_node


# # def tag_prep(products):
# #     handler = trie()
# #     listem = []
# #     holder = ""
# #     print(handler.root)

# #     for product in products:
# #         temp = []
# #         temps = product.split()
# #         for word in temps:
# #             upper = word.upper()
# #             temp.append(upper)
# #             print(temp)

# #         for words in temp:
# #             state = handler.is_word(words)
# #             print(state)
# #             if state:
# #                 holder = words
# #             else:
# #                 holder = "NULL"

# #         listem.append(holder)
# #         holder = ""

# #     print(listem)
# #     return listem


# # products = [
# #     "A48 WYSIWYG Premium Male Betta",
# #     "big ass baller brown kush doggy",
# #     "small ole fish",
# #     "big ole bear",
# #     "small ole bear",
# # ]
# # tag_prep(products)

# # bop = {"bop": "bap", "mop": "lap", "slop": "cap"}
# # print(bop)
