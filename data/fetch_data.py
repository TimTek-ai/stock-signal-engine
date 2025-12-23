import yfinance as yf

def get_price_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)
