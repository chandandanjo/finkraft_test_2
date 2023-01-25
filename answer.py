import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

output = []

def scrape(page_no):
    URL = f"https://www.nykaa.com/brands/nykaa-cosmetics/c/1937?page_no={page_no}&sort=popularity&utm_content=ads&utm_source=GooglePaid&utm_medium=PLA&utm_campaign=performancemaxnykaacosmetics&eq=desktop"
    try:
        resp = requests.get(URL)
        soup = BeautifulSoup(resp.content, 'lxml')
        prodDetails_names = [i.text for i in soup.find_all('div', {'class':'css-xrzmfa'})]
        prodDetails_prices = [i.text for i in soup.find_all('span', {'class':'css-111z9ua'})]
        prodDetails_ratedBy = [i.text for i in soup.find_all('span', {'class':'css-1j33oxj'})]
        
        for i in range(len(prodDetails_names)):
            output.append({
                'name':prodDetails_names[i],
                'price':prodDetails_prices[i],
                'ratedBy':prodDetails_ratedBy[i]
            })
        print('scraped page ', page_no)
    except Exception as e:
        print(e)
    sleep(2)


for i in range(1,15):
    scrape(i)

with open('output.csv', 'w+', newline='', encoding='utf-8') as output_file:
    keys = output[0].keys()
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(output)
    