import yfinance as yf
import pandas as pd
from datetime import datetime

theTicker = "MSFT"
data = yf.Ticker(theTicker)

data_balance = data.balance_sheet

data_balance.to_excel(f"{theTicker}_Balance_Sheet.xlsx")

data_div = data.dividends

print(data_div.index)
data_div.index= pd.to_datetime( data_div.index)
data_div.index= data_div.index.tz_localize(None)
data_div.to_excel(f"{theTicker}_Dividends.xlsx")