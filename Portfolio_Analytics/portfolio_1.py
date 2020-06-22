import csv
from yahoo_fin.stock_info import *

#Get tickers from CSV file

x, tickers = [], []
with open('tickers.csv', 'rt') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for item in spamreader:
		x.append(item)

for item in x:
	for item2 in item:
		tickers.append(item2)

print("tickers obtained")

# Get previous close and current prices for each of the tickers

previous_close, current_price = [], []

for ticker in tickers:
	previous_close_price = get_quote_table(ticker).get('Previous Close')
	previous_close.append(previous_close_price)

print("previous close obtained")
#previous close request is the rate limiting step here, as verified

for ticker in tickers:
	current_share_price = get_live_price(ticker)
	current_price.append(current_share_price)

print("current price obtained")

percentage_change = [(c/p)-1 for c,p in zip(current_price, previous_close)] 

print(percentage_change)