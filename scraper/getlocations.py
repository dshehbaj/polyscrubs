from requests import get
from bs4 import BeautifulSoup
from time import sleep

main_url = "http://washalert.washlaundry.com/washalertweb/calpoly/"

links = {
    "Cerro Vista" : "cerro-vista.html",
    "North Mountain" : "north-mountain.html",
    "PCV" : "poly-canyon-village.html",
    "Sierra Madre" : "sierra-madre-towers.html",
    "Red Bricks" : "south-mountain.html",
    "Yakitutu" : "ytt.html",
    "Yosemite" : "yosemite.html"
    }

def getLocations():
    locations = {}
    for key, value in links.items():
        locations[key] = {}
        data = get(main_url + value)
        soup = BeautifulSoup(data.text, "html.parser")
        for link in soup.find_all("a"):
            tokens = link.get("href").split("=")
            if len(tokens) == 2:
                locations[key][link.string] = tokens[1]
    return locations

if __name__ == "__main__":
    getLocations()
