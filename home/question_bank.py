QUESTION_BANK = {
    "self_awareness": [
        "What emotions would you experience in this situation?"
    ],
    "emotional_regulation": [
        "How would you manage your emotions before responding?"
    ],
    "empathy": [
        "How would you understand the other person's feelings?"
    ],
    "conflict_resolution": [
        "How would you resolve this conflict constructively?"
    ]
}

PROFESSION_CATEGORY_MAP = {
    "Software Engineer": ["self_awareness", "emotional_regulation", "conflict_resolution"],
    "Manager": ["empathy", "conflict_resolution", "emotional_regulation"],
    "Doctor": ["empathy", "emotional_regulation"],
    "Teacher": ["empathy", "self_awareness"]
}

SCENARIO_TEMPLATES = {
    "Software Engineer": [
        "You are facing a tight deadline and a teammate publicly criticizes your code quality.",
        "A production bug appears just before release, and stakeholders are pressuring you."
    ],
    "Doctor": [
        "A patient’s family is emotionally distressed and blaming you for treatment delays.",
        "You must deliver bad news to a patient while managing their emotional reaction."
    ],
    "Manager": [
        "Two team members are in conflict, affecting team productivity and morale."
    ]
}
