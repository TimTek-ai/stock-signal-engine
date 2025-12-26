import logging
from typing import Dict
from signals.momentum import momentum_signal
from signals.rsi import rsi_signal

# -------------------------
# Logging setup
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def calculate_confidence(
    signals: Dict[str, int],
    weights: Dict[str, float]
) -> dict:
    """
    signals:
        key   = signal name
        value = +1 (bullish), -1 (bearish), 0 (neutral)

    weights:
        key   = signal name
        value = importance weight (e.g. 0.4)

    returns:
        {
            "direction": "UP" | "DOWN" | "NEUTRAL",
            "confidence": float (0–100)
        }
    """

    if not signals:
        logger.warning("No signals provided.")
        return {"direction": "NEUTRAL", "confidence": 0.0}

    weighted_score = 0.0
    max_possible_score = 0.0

    for name, value in signals.items():
        weight = weights.get(name, 0)
        weighted_score += value * weight
        max_possible_score += abs(weight)

        logger.info(
            f"Signal={name} | Value={value} | Weight={weight}"
        )

    logger.info(f"Weighted score: {weighted_score}")
    logger.info(f"Max possible score: {max_possible_score}")

    # Direction
    if weighted_score > 0:
        direction = "UP"
    elif weighted_score < 0:
        direction = "DOWN"
    else:
        direction = "NEUTRAL"

    # Confidence (how strong the agreement is)
    confidence = (
        abs(weighted_score) / max_possible_score * 100
        if max_possible_score > 0
        else 0.0
    )

    confidence = round(confidence, 2)

    logger.info(f"Final direction: {direction}")
    logger.info(f"Confidence: {confidence}%")

    return {
        "direction": direction,
        "confidence": confidence
    }


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    signals = {
        "news_sentiment": 1,
        "momentum": 1,
        "volume": 0,
        "rsi": -1
    }

    weights = {
        "news_sentiment": 0.4,
        "momentum": 0.3,
        "volume": 0.2,
        "rsi": 0.1
    }

    result = calculate_confidence(signals, weights)
    print(result)
