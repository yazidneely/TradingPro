import yfinance as yf
dat = yf.Ticker("MSFT")

print(dat.info)

with open('my_file.json') as file:
    file.write(dat.info)

