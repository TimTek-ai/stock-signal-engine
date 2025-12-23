from data.fetch_data import get_price_data
from signals.simple_signal import simple_moving_average_signal

if __name__ == "__main__":
    ticker = "AAPL"
    data = get_price_data(ticker)

    signal = simple_moving_average_signal(data)
    print(f"{ticker} signal:", signal)
