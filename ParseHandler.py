from bs4 import BeautifulSoup
from lxml import etree, html
import json
import sqlite3
import os
from DBH import *


class DBT:
    # initialization-----------------------------------------------------------------------------------------------------
    def __init__(self, data_set, log_file, seller: str, links):
        self.data = data_set
        self.log_file = log_file
        self.seller = seller
        self.links = links
        output = self.data_prep(data_set, log_file)
        self.data_query(output,seller, links)

    #data prep / parsing -----------------------------------------------------------------------------------------------
    def data_prep(self, data_set, log_file):
        self.data_set = data_set
        self.log_file = log_file

        # Project File reading (for parse tasking)----------------------------------------------------------------------
        try:
            with open(log_file, 'r', encoding='utf-8') as file:
                _, ext = os.path.splitext(log_file) # separates extension for file check
                extensions = ['.html', '.xhtml']
                temp_set = []

                if ext in extensions:
                    for element in data_set:

                        element.decode('utf-8')
                        temp_set.append(element)

                        if not temp_set:
                            print('---HAND-OFF NOT ACCEPTED: DATA NOT PULLED FROM REQUEST---')
                    return temp_set


                elif ext == '.json':
                    temp_set = []
                    for element in data_set: #list of json nodes
                        string_json = json.dumps(element) # returns string of json node (key/value pairs)
                        parsedJson = json.loads(string_json) # returns python dictionary of key/value pairs
                        content = parsedJson['results'][0]['content'] # accesses content in nested dictionary
                        temp_set.append(content)
                        if not temp_set:
                            print('---HAND-OFF NOT ACCEPTED: DATA NOT PULLED FROM JSON---')
                    return temp_set

        except FileNotFoundError:
            print("---FILE HAND-OFF ERROR: MAKE SURE THIS FILE EXISTS---")
        except PermissionError:
            print('---INVALID PERMISSIONS ERROR: THE FILES PERMISSIONS WERE CHANGED IN THE OS DURING HAND-OFF---')
        except OSError as e:
            print(f"OS error: {e}")
        except Exception as e:
            print(f"AN UNEXPECTED ERROR OCCURED AT HANDOFF: {e}")


    #query manager ----------------------------------------------------------------------------------------------------
    def data_query(self, temp_data, seller: str, links):
        self.links = links
        self.seller = seller
        prices = []
        product = []
        description = []
        price_query = ''
        title_query = ''
        while True:
            price_query = input('\nEnter class name for product price (Found within HTML code of any product: '.format())
            title_query = input('Enter class name for product Title (Found within HTML code of any product: ')


            if price_query != '' and title_query != '':
                break

            else: print("INVALID")

        desc_query = input('Enter class name for product Description (Found within HTML code of any product: ')

        for element in temp_data:
            soup = BeautifulSoup(element, 'lxml')
            title_tag = soup.title
            price_result = soup.find(class_='{}'.format(price_query))
            title_result = soup.find(class_='{}'.format(title_query))

            if desc_query != None:
                description_result = soup.find('span', attrs={desc_query: True})
                if description_result:
                    desc_text = description_result.text
                else:
                    desc_text = " Description: N/A"
                description.append(desc_text)
            else:
                description.append("N/A")

            if price_result:
                prices.append(price_result.text)
            else:
                prices.append('NULL')
            if title_result:
                product.append(title_result.text)
            else: product.append('NULL')




            print(title_result.text)
            print(price_result.text)
            print(desc_text)

        dbh = DatabaseHandler(seller,product,prices, description, links)

    def tag_prep (self, products):
        handler = trie()
        for product in products:
            for word in product.split():
                print(word)

            #is_listed = handler.is_word(product)
            #if is_listed:













