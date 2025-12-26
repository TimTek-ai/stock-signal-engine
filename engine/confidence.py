import logging
from signals.rsi import rsi_signal

logger = logging.getLogger(__name__)

def calculate_confidence(ticker: str) -> int:
    """
    Returns confidence score from 0 to 100
    based on available signals
    """

    score = 0
    max_score = 0

    try:
        # RSI signal
        rsi = rsi_signal(ticker)
        max_score += 1

        if rsi == 1:
            score += 1
        elif rsi == -1:
            score += 0
        else:
            score += 0.5  # neutral gets partial credit

        confidence = int((score / max_score) * 100)

        logger.info(f"{ticker} confidence score: {confidence}")
        return confidence

    except Exception as e:
        logger.error(f"Confidence calculation failed: {e}")
        return 0
