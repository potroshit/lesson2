import requests
from bs4 import BeautifulSoup as BS
from time import sleep

def get_url():
    for pege in range(1,8):
        sleep(1)
        url = f"https://scrapingclub.com/exercise/list_basic/?page={pege}"
        response = requests.get(url)
        soup = BS(response.text, "lxml")
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

        for i in data:
            url_img = 'https://scrapingclub.com'+i.find('a').get('href')
            yield url_img


for i in get_url():
    response = requests.get(i)
    soup=BS(response.text, 'lxml')
    data = soup.find_all('div', class_='card mt-4 my-4')

    for j in data:
        name = j.find('h3', class_='card-title').text.strip()
        price = j.find('h4').text.strip()
        text = j.find('p', class_='card-text').text
        print(name+'\n'+price+'\n'+text+'\n'+i)
        print()
        print()