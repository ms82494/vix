import os
import pandas as pd

csv_folder = "./csv_files"

for file in os.listdir(csv_folder):
    if file.startswith("VX"):
        fullname = os.path.join(csv_folder, file)
        vix = pd.read_csv(
            fullname,
            index_col=0,
            parse_dates=True,
            usecols= [0,1,2,3,4,5,6,7,8,9,10],
            header=0,
            names=['date', 'contract', 'open', 'high', 'low', 'close', 'settle','change', 'volume', 'efp', 'openinterest']
            )
        newfile = vix.index.max().isoformat()[0:10] + ".csv"
        os.rename(fullname, os.path.join(csv_folder, newfile))


