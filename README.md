# vix
This repo downloads daily VIX future pricing histories from the CBOE website, for future analysis. Each contract's price history is kept in a separate csv file, named with the expiration dates. It includes both monthly and weekly futures contracts. Updating the history should only require running the ```update_csv.py``` file in a python interpreter.
