from bs4 import BeautifulSoup
from time import sleep
import requests as req
import getLocations as gl
import getMachines as gm

wash_alert = "http://washalert.washlaundry.com/washalertweb/calpoly/WASHALERtweb.aspx?location="

def getData():
    machine_urls = {}
    machine_data = {}
    locations = gl.getLocations()
    for location in locations.keys():
        for building in locations[location].keys():
            url = wash_alert + locations[location][building]
            key = location.lower().strip() + '_' + building.lower().strip()
            key = key.replace(' ', '-')
            key = key.replace('---', '-') #Needed For Yakitutu Buildings
            machine_urls[key] = url
    for location, locUrl in machine_urls.items():
        tokens = location.split('_')
        info = gm.getMachines(locUrl, tokens[0], tokens[1])
        machine_data[location] = info
    return machine_data

if __name__ == "__main__":
    data = getData()
    for location, buildings in data.items():
        print(f'{location}: {buildings}')
