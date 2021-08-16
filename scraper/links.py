from bs4 import BeautifulSoup
import requests as req
import getlocations as gl

wash_alert = "http://washalert.washlaundry.com/washalertweb/calpoly/WASHALERtweb.aspx?location="
machines = {}

def main():
    locations = gl.getLocations()
    for location in locations.keys():
        for building in locations[location].keys():
            url = wash_alert + locations[location][building]
            key = location.lower().strip() + ' ' + building.lower().strip()
            key = key.replace(' ', '-')
            key = key.replace('---', '-') #For Yakitutu Buildings
            machines[key] = url
    print(machines)

if __name__ == "__main__":
    main()
