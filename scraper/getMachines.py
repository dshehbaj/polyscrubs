from bs4 import BeautifulSoup
from requests import get

def getMachines(link: str):
    data = get(link)
    soup = BeautifulSoup(data.text, 'html.parser')
    for tr in soup.find_all("tr", {'class': lambda x: x and x.startswith('Machine')}):
        names = tr.findChildren('td', {'class': 'name'}, recursive='false')
        types = tr.findChildren('td', {'class': 'type'}, recursive='false')
        statuses = tr.findChildren('td', {'class': 'status'}, recursive='false')
        times = tr.findChildren('td', {'class': 'time'}, recursive='false')
        data = []
        for name in names:
            data.append(name.text.strip())
        for type in types:
            data.append(type.text.strip())
        for status in statuses:
            data.append(status.text.strip())
        for time in times:
            data.append(time.text.strip())
        return data


if __name__ == "__main__":
    getMachines()

