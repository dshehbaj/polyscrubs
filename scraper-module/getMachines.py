"""
Function that returns all the machine data for a given building in a complext.
@author Shehbaj
"""

from bs4 import BeautifulSoup
from requests import get
from time import sleep, time
from random import randint

def getMachines(link: str, complex: str, bldg: str):
    sleep(3)
    CURRENT_TIME = str(int(time() * 1000))
    data = get(link)
    soup = BeautifulSoup(data.text, 'html.parser')
    machineList = []
    for tr in soup.find_all("tr", {'class': lambda x: x and x.startswith('Machine')}):
        names = tr.findChildren('td', {'class': 'name'}, recursive='false')
        types = tr.findChildren('td', {'class': 'type'}, recursive='false')
        statuses = tr.findChildren('td', {'class': 'status'}, recursive='false')
        dimension = []
        record = {}
        dimension.append({'Name': 'complex', 'Value': complex})
        dimension.append({'Name': 'building', 'Value': bldg})
        for type in types:
            dimension.append({'Name': 'type', 'Value': type.text.strip().lower().replace(' ', '-')})
        for name in names:
            dimension.append({'Name': 'number', 'Value': name.text.strip().lower().replace(' ', '-')})
        record['Time'] = CURRENT_TIME
        record['Dimensions'] = dimension
        record['MeasureName'] = 'status'
        record['MeasureValueType'] = 'VARCHAR'
        for status in statuses:
            record['MeasureValue'] = status.text.strip().lower().replace(' ', '-')
        machineList.append(record)
    return machineList


if __name__ == "__main__":
    link = 'http://washalert.washlaundry.com/washalertweb/calpoly/WASHALERtweb.aspx?location=64f22163-821e-4b46-8194-73e5559f6668'
    complex = 'cerrovista'
    bldg = 'morro'
    records = getMachines(link, complex, bldg)
    for record in records:
        print(record)

