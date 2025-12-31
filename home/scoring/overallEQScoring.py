CATEGORY_WEIGHTS = {
    "self_awareness": 0.2,
    "emotional_regulation": 0.25,
    "empathy": 0.2,
    "conflict_resolution": 0.2,
    "motivation": 0.15,
    "social_skills":0.2
}


def calculate_overall_eq(category_scores):
    overall = 0.0

    for category, weight in CATEGORY_WEIGHTS.items():
        overall += category_scores.get(category, 0) * weight

    overall = round(overall, 2)

    if overall < 50:
        level = "Low EQ"
    elif overall < 75:
        level = "Average EQ"
    else:
        level = "High EQ"

    return overall, level
