import os
import requests
from datetime import datetime

from bs4 import BeautifulSoup

url = 'https://www.cboe.com/us/futures/market_statistics/historical_data/'
csv_url = "https://www.cboe.com/us/futures/market_statistics/historical_data/products/csv/VX/"
today = datetime.today().isoformat()[0:10] + "\n"
last_update_file = "./last_update"
download_folder = './csv_files'

# read the date of the last update from the last_update file
with open(last_update_file, "r") as file:
    last_update = file.readline().strip("\n")
    file.close()


r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

all_hrefs = soup.find_all('a')                                              # find all HTML links on the CBOE page
all_links = [link.get('href') for link in all_hrefs]                        # get the URLs of the links
csv_files = [dl for dl in all_links if 'products/csv/VX' in dl]             # filter out all links that don't point to VX price histories
expiration_dates = [csv_file.split("/")[-2] for csv_file in csv_files]      # simplify the list contents to the dates
update_dates = [date for date in expiration_dates if date >= last_update]   # filter out all those contracts that expired before last update
                                                                            # since these don't need to be updated

# iterate over the expiration dates of contracts that had not expired as of the last update
# and (over)write their respective price history files
for update_date in update_dates:
    full_url = csv_url + update_date
    r = requests.get(full_url)
    csv_filename = update_date + ".csv"
    dl_path = os.path.join(download_folder, csv_filename)
    with open(dl_path, 'wb') as csv:
        csv.write(r.content)

#updates the last_update file with the today's date.
with open(last_update_file, "w") as file:
    last_update = file.writelines(today)
    file.close()
