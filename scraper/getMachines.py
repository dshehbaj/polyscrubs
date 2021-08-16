from bs4 import BeautifulSoup
from requests import get

def getMachines(link: str):
    data = get(link)
    soup = BeautifulSoup(data.text, 'html.parser')
    machineList = []
    for tr in soup.find_all("tr", {'class': lambda x: x and x.startswith('Machine')}):
        names = tr.findChildren('td', {'class': 'name'}, recursive='false')
        types = tr.findChildren('td', {'class': 'type'}, recursive='false')
        statuses = tr.findChildren('td', {'class': 'status'}, recursive='false')
        times = tr.findChildren('td', {'class': 'time'}, recursive='false')
        machine = []
        for name in names:
            machine.append(name.text.strip())
        for type in types:
            machine.append(type.text.strip())
        for status in statuses:
            machine.append(status.text.strip())
        for time in times:
            machine.append(time.text.strip())
        machineList.append(machine)
    return machineList


if __name__ == "__main__":
    link = 'http://washalert.washlaundry.com/washalertweb/calpoly/WASHALERtweb.aspx?location=64f22163-821e-4b46-8194-73e5559f6668'
    print(getMachines(link))

