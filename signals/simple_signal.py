def simple_moving_average_signal(data, window=20):
    data["SMA"] = data["Close"].rolling(window).mean()

    latest_price = data["Close"].iloc[-1]
    latest_sma = data["SMA"].iloc[-1]

    if latest_price > latest_sma:
        return "BULLISH"
    else:
        return "BEARISH"
