from yahoo_fin.stock_info import *
import csv

# style.use('dark_background')
ticker = 'aapl'

dict_data = get_quote_table(ticker)

csv_file = str(ticker)+'_data.csv'

with open(csv_file,'w') as f:
    w = csv.writer(f)
    w.writerow(dict_data.keys())
    w.writerow(dict_data.values())