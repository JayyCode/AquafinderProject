# ---------------imports------------------------------------------------------------------------------------------------
import random
import sys
import time
import requests
from requests.exceptions import (
    RequestException,
)  # for error handling in the first try/catch block
from lxml import etree
from pprint import pprint
from ParseHandler import DBT
from urllib.parse import urlparse  # for parsing  url
import json


# ---------------Class Establishment------------------------------------------------------------------------------------
class scaperAPI:

    # ---------------Initialization(Link tree Header)/Function Automation-----------------------------------------------

    def __init__(self, url, filter_key=None, nsURL=None):

        self.url = url
        self.nsURL = nsURL
        self.filter_key = filter_key

        self.taskRoute(url, nsURL, filter_key)

    # ---------------Init Scrape(Link tree Header)----------------------------------------------------------------------

    def initScrape(self, url, nsURL=None, filter_key=None):
        self.url = url
        self.nsURL = nsURL
        self.filter_key = filter_key

        # ---------------HTTPS Connection Check-------------------------------------------------------------------------
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            # ---------------Request Check & Response Parsing---------------------------------------------------------------
            if response.status_code == 200 or response.status_code == 202:

                xml_dataformat = response.content.decode("utf-8")
                xml_data = response.content
                xpath_dir = (
                    '//ns:loc[contains(text(), "{}")]/text()'.format(filter_key)
                    if filter_key
                    else "//ns:loc/text()"
                )
                tree = etree.fromstring(xml_data)

                nsmap = {
                    "ns": "http://www.sitemaps.org/schemas/sitemap/0.9",
                    "imgns": "http://www.google.com/schemas/sitemap-image/1.1",
                    "xhtml": "http://www.w3.org/1999/xhtml",
                }

                hyperlinks = tree.xpath(
                    xpath_dir, namespaces=nsmap
                )  # returns a list for the variable

                # the loop in the brackets is the nested if statement. read it backwards
                filtered_urls = (
                    [link for link in hyperlinks if filter_key in link]
                    if filter_key
                    else hyperlinks
                )  # Filter URLs based on the specified keyword

                # ---------------Response Content Check & Print ------------------------------------------------------------
                if not len(filtered_urls) == 0:

                    for hyperlink in filtered_urls:
                        print(hyperlink)
                    print("DATA RETREIVAL SUCCESS: RESPONSE CODE (200)")

                    return filtered_urls

                else:
                    print("DATA RETREIVAL ERROR: CHECK NAMESPACE URL")

            else:
                print(
                    "No valid response from server.. retreived code: "
                    + str(response.status_code)
                )
        except RequestException as e:
            print(
                "------------------------------------------"
                "INVALID HTTPS CONNECTION: CHECK TARGET URL"
                "------------------------------------------"
            )

    # ----------------Scraper Clock (Link Tree)-------------------------------------------------------------------------

    def scrapeClock(self, filtered_urls):

        htmldata = []  # list for log data
        count = 0
        length = len(filtered_urls)

        # Clock tasks---------------------------------------------------------------------------------------------------
        for hyperlink in filtered_urls:
            response_delay: float = round(random.randint(0, 2) * random.random(), 2)

            html = self.mainScrape(hyperlink)  # returns data for each link scrapped
            htmldata.append(html)  # adds return data to log list
            count = count + 1
            self.progress(count, length)

            time.sleep(response_delay)

        return htmldata

    # ----------------Link Scraper (Link Tree)--------------------------------------------------------------------------

    def mainScrape(self, link):
        self.link = link

        try:
            response = requests.get(link)
            html_data = response.content
            response.raise_for_status()  # Raises an HTTPError for bad responses
            data = response.content.decode("utf-8", "ignore")

            return html_data

        except RequestException as e:
            print("----------" "INVALID HTTPS CONNECTION" "----------")
            print("UNABLE TO RETRIEVE LINK " + self.link)

    # ----------------Task Router (Control Center)----------------------------------------------------------------------
    def taskRoute(self, url, nsURL=None, filter_key=None):
        self.url = url
        self.nsURL = nsURL
        self.filter_key = filter_key

        # URL Domain Name Extraction-------------------------------------------------------------------------------------
        parsed_url = urlparse(url)  # Split the url into parts and returns them in list
        domain_parts = parsed_url.netloc.split(
            "."
        )  # Split the domain name into parts based off periods
        seller_name = domain_parts[-2] if len(domain_parts) >= 2 else domain_parts[-1]

        # Program Prompt
        ans = input("Send Task Through SmartProxy? Y/N:  ")

        if ans == "Y" or ans == "y":
            links = self.initScrape(
                url, nsURL, filter_key
            )  # (returns link tree header)

            # SP API Request--------------------------------------------------------------------------------------------
            url = "https://scrape.smartproxy.com/v1/tasks"
            log_data = []
            count = 0
            length = len(links)

            for link in links:
                payload = {"target": "universal", "url": link}
                headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": "Base64 encoded U0000142550:PW107283e45d5223036a149c85891e200ca",
                }
                response = requests.post(
                    url,
                    json=payload,
                    auth=("U0000142550", "PW107283e45d5223036a149c85891e200ca"),
                )

                # storing requests (json nodes)---------------------------------------------------------------------
                json_data = response.json()
                log_data.append(json_data)
                count = count + 1
                self.progress(count, length)

            # file naming / creation------------------------------------------------------------------------------------
            path = "{}.json".format(seller_name)  # file naming

            with open(path, "w", encoding="utf-8") as file:
                for node in log_data:
                    file.write(json.dumps(node))

            DB_Object = DBT(log_data, path, seller_name, links)

        elif ans == "N" or ans == "n":
            # Initial Scrape (returns encoded html)---------------------------------------------------------------------
            links = self.initScrape(url, nsURL, filter_key)

            # Tree Scrape w/ limiter clock (Returns encoded html)-------------------------------------------------------
            data = self.scrapeClock(links)

            path = "{}.html".format(seller_name)

            # Log Writer (logs all scdraper activity to view)-----------------------------------------------------------
            with open(path, "w", encoding="utf-8") as file:
                for html_data in data[:]:
                    if html_data is None:
                        data.remove(html_data)
                    else:
                        file.write(html_data.decode("utf-8", "ignore"))

            DB_Object = DBT(data, path, seller_name, links)

        else:
            print("Invalid")

    # Progress Bar-------------------------------------------------------------------------------------------------------
    def progress(self, count, length):
        self.length = length
        progress = round(count / length * 100, 2)

        if progress <= 100:
            sys.stdout.write("'\r[PROGRESS] {}%".format(progress, end=""))
        else:
            print("DATA RETREIVAL COMPLETE")
