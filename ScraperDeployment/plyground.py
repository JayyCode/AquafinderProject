import datetime


date = datetime.datetime.today()
print(date)


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


def tag_prep(products):
    handler = trie()
    listem = []
    holder = ""
    print(handler.root)

    for product in products:
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


products = [
    "A48 WYSIWYG Premium Male Betta",
    "big ass baller brown kush doggy",
    "small ole fish",
    "big ole bear",
    "small ole bear",
]
tag_prep(products)

bop = {"bop": "bap", "mop": "lap", "slop": "cap"}
print(bop)
