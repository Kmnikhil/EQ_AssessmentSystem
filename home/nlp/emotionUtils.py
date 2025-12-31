POSITIVE_EMOTIONS = ["joy"]
NEGATIVE_EMOTIONS = ["anger", "sadness", "fear", "disgust"]
NEUTRAL_EMOTIONS = ["neutral"]


def emotional_breakdown(model_output):
    positive, negative, neutral = 0.0, 0.0, 0.0

    for item in model_output:
        label = item["label"].lower()
        score = item["score"]

        if label in POSITIVE_EMOTIONS:
            positive += score
        elif label in NEGATIVE_EMOTIONS:
            negative += score
        elif label in NEUTRAL_EMOTIONS:
            neutral += score

    total = positive + negative + neutral

    if total == 0:
        return {"positive": 0, "negative": 0, "neutral": 0}

    return {
        "positive": round((positive / total) * 100, 2),
        "negative": round((negative / total) * 100, 2),
        "neutral": round((neutral / total) * 100, 2),
    }
