EMOTION_WEIGHTS = {
    "positive": 1.0,
    "neutral": 0.6,
}

CATEGORY_EMOTION_WEIGHTS = {
    "self_awareness": {"negative": 0.6},
    "emotional_regulation": {"negative": 0.2},
    "empathy": {"negative": 0.4},
    "conflict_resolution": {"negative": 0.2},
    "motivation": {"negative": 0.2},
    "social_skills":{"negative":0.2}
}

def calculate_EQScore(category,breakdown):
    negative_weight = CATEGORY_EMOTION_WEIGHTS.get(category, {}).get("negative", 0.2)

    ### EQ score calculation
    eq_score = (
        breakdown["positive"] * EMOTION_WEIGHTS["positive"] +
        breakdown["neutral"] * EMOTION_WEIGHTS["neutral"] +
        breakdown["negative"] * negative_weight
    ) / 100     
    
    return round(eq_score * 100, 2)