def aggregate_category_scores(category_responses):
    """
    category_responses = {
        "empathy": [72, 78],
        "emotional_regulation": [65, 70]
    }
    """
    final_scores = {}

    for category, scores in category_responses.items():
        final_scores[category] = round(sum(scores) / len(scores), 2)

    return final_scores
