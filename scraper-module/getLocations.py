"""
Function to return all the location IDs for all the buildings in each complex.
@author Shehbaj Dhillon
"""

from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint

main_url = "http://washalert.washlaundry.com/washalertweb/calpoly/"

links = {
    "CerroVista" : "cerro-vista.html",
    "NorthMountain" : "north-mountain.html",
    "PCV" : "poly-canyon-village.html",
    "SierraMadre" : "sierra-madre-towers.html",
    "RedBricks" : "south-mountain.html",
    "Yakitutu" : "ytt.html",
    "Yosemite" : "yosemite.html"
    }

def getLocations():
    locations = {}
    for key, value in links.items():
        locations[key] = {}
        sleep(randint(3, 5))
        data = get(main_url + value)
        soup = BeautifulSoup(data.text, "html.parser")
        for link in soup.find_all("a"):
            tokens = link.get("href").split("=")
            if len(tokens) == 2:
                locations[key][link.string] = tokens[1]
    return locations

if __name__ == "__main__":
    data = getLocations()
    for key, value in data.items():
        print(f'{key}: {value}')
