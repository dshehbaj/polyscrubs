from bs4 import BeautifulSoup
from time import sleep
import requests as req
import getLocations as gl
import getMachines as gm

wash_alert = "http://washalert.washlaundry.com/washalertweb/calpoly/WASHALERtweb.aspx?location="

def getData():
    numMachines = 0
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
        info = gm.getMachines(locUrl, location)
        machine_data[location] = info[0]
        numMachines += info[1]
    return (machine_data, numMachines)

if __name__ == "__main__":
    data = getData()
    machineIDs = []
    for location, buildings in data[0].items():
        for bldg in buildings:
            machineIDs.append(bldg[0])
        print(f'{location}: {buildings}')
    print(f'there are {data[1]} machines in total')
    print(f'Machines ID: {machineIDs}')
