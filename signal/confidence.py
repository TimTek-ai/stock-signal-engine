def calculate_confidence(sentiment_score, signal_strength, volatility):
    """
    sentiment_score: float between -1 and 1
    signal_strength: float between 0 and 1
    volatility: float between 0 and 1 (higher = more risky)
    """

    # Base confidence from sentiment + signal agreement
    base_confidence = (
        abs(sentiment_score) * 0.5 +
        signal_strength * 0.5
    )

    # Penalise high volatility
    volatility_penalty = volatility * 0.4

    confidence = base_confidence - volatility_penalty

    # Clamp between 0 and 1
    confidence = max(0.0, min(confidence, 1.0))

    # Convert to percentage
    return round(confidence * 100, 2)
