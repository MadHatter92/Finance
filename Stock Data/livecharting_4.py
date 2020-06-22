import sys
from yahoo_fin.stock_info import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
from datetime import datetime as dt
import datetime
import pandas as pd

style.use('dark_background')

ticker = sys.argv[1]
today = dt.today().strftime("%m/%d/%Y")
# one_week_start_date = (dt.today() - datetime.timedelta(days=7)).strftime("%m/%d/%Y")
one_month_start_date = (dt.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y")
one_year_start_date = (dt.today() - datetime.timedelta(days=365)).strftime("%m/%d/%Y")
five_year_start_date = (dt.today() - datetime.timedelta(days=365*5)).strftime("%m/%d/%Y")
ten_year_start_date = (dt.today() - datetime.timedelta(days=365*10)).strftime("%m/%d/%Y")

figure, axes = plt.subplots(1,4)

# plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.01, hspace=0.001)
# figure.tight_layout()
# plt.margins(x=0.05, y=0.05, tight=True)

# one_week_data = pd.DataFrame(get_data(ticker , start_date = one_week_start_date, end_date = today))
# one_week_data.plot(ax = axes[0], kind = 'line', y = 'adjclose', title = '1 week', legend = None)

one_month_data = pd.DataFrame(get_data(ticker , start_date = one_month_start_date, end_date = today))
one_month_data.plot(ax = axes[0], kind = 'line', y = 'adjclose', title = '1 month', legend = None)

one_year_data = pd.DataFrame(get_data(ticker , start_date = one_year_start_date, end_date = today))
one_year_data.plot(ax = axes[1], kind = 'line', y = 'adjclose', title = '1 year', legend = None)

five_year_data = pd.DataFrame(get_data(ticker , start_date = five_year_start_date, end_date = today))
five_year_data.plot(ax = axes[2], kind = 'line', y = 'adjclose', title = '5 year', legend = None)

ten_year_data = pd.DataFrame(get_data(ticker , start_date = ten_year_start_date, end_date = today))
ten_year_data.plot(ax = axes[3], kind = 'line', y = 'adjclose', title = '10 year', legend = None)

figure.suptitle(ticker, fontsize = 16)
plt.show()