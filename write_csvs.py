import os
import requests

from bs4 import BeautifulSoup

url = 'https://www.cboe.com/us/futures/market_statistics/historical_data/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

all_hrefs = soup.find_all('a')
all_links = [link.get('href') for link in all_hrefs]
csv_files = [dl for dl in all_links if 'products/csv/VX' in dl]
download_folder = './csv_files'

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

for csv_file in csv_files:
    full_url = url + csv_file
    r = requests.get(full_url)
    csv_filename = csv_file.split("/")[-2] + ".csv"
    dl_path = os.path.join(download_folder, csv_filename)
    with open(dl_path, 'wb') as csv:
        csv.write(r.content)