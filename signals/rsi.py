import yfinance as yf
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def rsi_signal(ticker: str, period: int = 14) -> int:
    """
    RSI-based signal:
    +1 if RSI < 30 (oversold)
    -1 if RSI > 70 (overbought)
     0 otherwise
    """

    try:
        data = yf.download(
            ticker,
            period="3mo",
            interval="1d",
            progress=False
        )

        if data.empty or len(data) < period:
            logger.warning("Not enough data for RSI.")
            return 0

        close = data["Close"]

        delta = close.diff()
        gain = delta.where(delta > 0, 0.0)
        loss = -delta.where(delta < 0, 0.0)

        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # ✅ Correct, future-proof way
        latest_rsi = rsi.iloc[-1].item()

        logger.info(f"{ticker} RSI: {latest_rsi:.2f}")

        if latest_rsi < 30:
            return 1
        elif latest_rsi > 70:
            return -1
        else:
            return 0

    except Exception as e:
        logger.error(f"RSI signal failed: {e}")
        return 0
