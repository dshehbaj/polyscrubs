from bs4 import BeautifulSoup
from requests import get

def getMachines(link: str, key: str):
    data = get(link)
    soup = BeautifulSoup(data.text, 'html.parser')
    machineList = []
    numMachines = 0
    for tr in soup.find_all("tr", {'class': lambda x: x and x.startswith('Machine')}):
        names = tr.findChildren('td', {'class': 'name'}, recursive='false')
        types = tr.findChildren('td', {'class': 'type'}, recursive='false')
        statuses = tr.findChildren('td', {'class': 'status'}, recursive='false')
        times = tr.findChildren('td', {'class': 'time'}, recursive='false')
        machine = []
        machineInfo = key
        for type in types:
            machineInfo += ('_' + type.text.strip().lower().replace(' ', '-'))
        for name in names:
            machineInfo += ('_' + name.text.strip().lower().replace(' ', '-'))
            numMachines += 1
        machine.append(machineInfo)
        for status in statuses:
            machine.append(status.text.strip().lower().replace(' ', '-'))
        for time in times:
            machine.append(time.text.strip().lower().replace(' ', '-'))
        machineList.append(machine)
    return (machineList, numMachines)


if __name__ == "__main__":
    link = 'http://washalert.washlaundry.com/washalertweb/calpoly/WASHALERtweb.aspx?location=64f22163-821e-4b46-8194-73e5559f6668'
    key = 'cerrovista_morro'
    print(getMachines(link, key))

