import yfinance as yf

stock = yf.Ticker("RELIANCE.NS")
price = stock.history(period="1d")["Close"][0]

if price > 2500:
    print("SELL RELIANCE STOCK!")
else:
    print("BUY RELIANCE STOCK!")
