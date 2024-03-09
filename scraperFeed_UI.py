
import requests
from lxml import etree


# from(library) import(class)

def handleLink(url, nsURL=None, filter_key=None):
    url = url
    response = requests.get(url)
    xml_dataformat = response.content.decode('utf-8')
    xml_data = response.content
    xpath_dir = '//ns:loc[contains(text(), "{}")]/text()'.format(filter_key) if filter_key else '//ns:loc/text()'

    # prints the code in the utf-8 format
    #// print(xml_dataformat)

    # Parse the XML data
    tree = etree.fromstring(xml_data)

    # inits the namespace var before generalizing it
    nsmap = {"ns": nsURL} if nsURL else {}

    # generalizes the actual namespace, and
    hyperlinks = tree.xpath(xpath_dir, namespaces=nsmap)

    # Filter URLs based on the specified keyword
    # the loop in the brackets is the nested if statement. read it backwards
    filtered_urls = [link for link in hyperlinks if filter_key in link] if filter_key else hyperlinks



    for hyperlink in filtered_urls:
        print(hyperlink)


handleLink('https://www.reefcleaners.org/sitemap.xml', "http://www.sitemaps.org/schemas/sitemap/0.9", 'store')







