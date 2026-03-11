import re

# Positive Rules
positive_rules = {
    "excellent": 3,
    "amazing": 2,
    "good": 1,
    "happy": 2,
    "love": 2
}

# Negative Rules
negative_rules = {
    "terrible": -3,
    "bad": -1,
    "worst": -2,
    "error": -2,
    "hate": -2
}


def calculate_sentiment(chunk):

    score = 0

    words = re.findall(r"\b\w+\b", chunk.lower())

    for w in words:
        score += positive_rules.get(w, 0) + negative_rules.get(w, 0)

    if score > 0:
        tag = "positive"
    elif score < 0:
        tag = "negative"
    else:
        tag = "neutral"

    return score, tag
