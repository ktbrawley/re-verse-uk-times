import requests
from bs4 import BeautifulSoup

reverse_uk_url = "https://www.residentevil.com/reverse/uk/topic/cbt/"
page = requests.get(reverse_uk_url)
soup = BeautifulSoup(page.content, 'html.parser')
timeEls = soup.find_all(class_="mb5 ind1")[:4]

for timeEl in timeEls:
    print(timeEl.text)

input("Press enter to exit...")
