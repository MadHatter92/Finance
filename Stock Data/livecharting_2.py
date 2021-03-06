
from yahoo_fin.stock_info import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime

style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ticker = "indy"
previous_close = get_quote_table(ticker).get('Previous Close')

xs = []
ys = []

def animate(i):
	# graph_data = open('example.txt', 'r').read()
	# lines = graph_data.split('\n')
	global x
	x = datetime.now().strftime("%H:%M")
	y = float(get_live_price(ticker))
	print(x,y)
	xs.append(x)
	ys.append(y)
	ax1.clear()
	ax1.plot(xs, ys)
	ax1.set_ylim([min(ys)*.998, max(ys)*1.002])
	ax1.set_title(ticker + " " + "{:.2%}".format(y/previous_close-1))
	plt.xticks(rotation='vertical')

ani = animation.FuncAnimation(fig, animate, interval = 1000*60)
plt.show()
# print(data)