import os
import requests as rq

from bs4 import BeautifulSoup

url = 'https://www.cboe.com/us/futures/market_statistics/historical_data/archive'
download_folder = './csv_files'

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

r = rq.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

all_hrefs = soup.find_all('a')
all_links = {
    href.text.replace(" ","").replace("\n","").replace("(","-").replace(")",""):
    href.get('href')
    for href in all_hrefs
    if ('VX ' in href.text) & ("Cboe" not in href.text)
    }

for text, link in all_links.items():
    r = rq.get(link)
    dl_path = os.path.join(download_folder, text + ".csv")
    with open(dl_path, 'wb') as csv:
        csv.write(r.content)
