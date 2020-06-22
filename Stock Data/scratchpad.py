# from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table
# nflx = get_data("NFLX")
# print(nflx)
# info = get_quote_table("amzn")
# print(info)

from yahoo_fin.stock_info import *
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style

# style.use('fivethirtyeight')

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)


# ticker = "NFLX"
# data = get_live_price(ticker)
# print(data)

print(get_quote_table('aapl').get('Previous Close'))