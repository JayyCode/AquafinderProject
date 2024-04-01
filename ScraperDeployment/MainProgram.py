from RequestHandler import scaperAPI


reef_cleaners = scaperAPI(
    "https://www.tacwearusa.com/sitemap_products_1.xml?from=6701843480762&to=6755803857082",
    "products",
)
