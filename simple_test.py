import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# dat = yf.Ticker("MSFT")

# print(dat.info)

# with open('my_file.json') as file:
#     file.write(dat.info)

data = yf.download(["MSFT","TSLA","AAPL"],start="2022-01-01", end="2025-06-27")

data["Close"].plot(title="Close Prices Big 3")
plt.show()

