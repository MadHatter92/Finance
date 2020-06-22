import csv
# import sys
from yahoo_fin.stock_info import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.ticker as mtick
from datetime import datetime

style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#Get tickers from CSV file

def get_tickers():
	x, tickers = [], []
	with open('portfolio.csv', 'rt') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for item in spamreader:
			x.append(item)

	for item in x:
		for item2 in item:
			tickers.append(item2)

	return(tickers)

# Get previous close and current prices for each of the tickers

tickers = get_tickers()

previous_close = []

for ticker in tickers:
	previous_close_price = get_quote_table(ticker).get('Previous Close')
	previous_close.append(previous_close_price)

# print("previous close obtained")
#previous close request is the rate limiting step here, as verified

def get_current_price(current_price):
	for ticker in tickers:
		current_share_price = get_live_price(ticker)
		current_price.append(current_share_price)
	# print(current_price)
	return(current_price)

# print("current price obtained")

def animate(i):
	ax1.clear()
	fig.suptitle(datetime.now().strftime("%b %d %Y %H:%M:%S"))
	current_price = []
	color = []
	percentage_change = [(c/p)-1 for c,p in zip(get_current_price(current_price), previous_close)]
	ax1.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
	# print(percentage_change)
	for item in percentage_change:
		if item >0:
			color.append('g')
		else:
			color.append('r')
	ax1.bar(tickers, percentage_change, color = color)
	rects = ax1.patches
	for rect, percentage in zip(rects, percentage_change):
	    height = rect.get_height()
	    ax1.text(rect.get_x() + rect.get_width() / 2, height, "{0:0.2%}".format(percentage), ha='center', va='bottom')
	plt.xticks(rotation='vertical')

ani = animation.FuncAnimation(fig, animate, interval = 1000*60)
plt.show()