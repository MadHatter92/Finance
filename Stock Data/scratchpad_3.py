
company_list = ['Netflix', 'Apple', 'Facebook']
ticker_list = ['NFLX', 'AAPL', 'FB']

options = [{'label': company, 'value': ticker} for (company, ticker) in zip(company_list, ticker_list)]
print(options)
