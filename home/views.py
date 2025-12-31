from django.shortcuts import render, redirect
from transformers import pipeline
from .nlp.emotion_detect_model import EmotionAnalyzer
from .nlp.emotionUtils import emotional_breakdown
from .scoring.categoryScoring import aggregate_category_scores
from .scoring.overallEQScoring import calculate_overall_eq
from .scoring.EQScoring import calculate_EQScore
from .question_bank import QUESTION_BANK, PROFESSION_CATEGORY_MAP, SCENARIO_TEMPLATES
import random
import matplotlib.pyplot as plt
import os
import uuid
from django.conf import settings


def user_info(request):
    if request.method == "POST":
        request.session["age"] = request.POST.get("age")
        request.session["gender"] = request.POST.get("gender")
        request.session["profession"] = request.POST.get("profession")

        return redirect("questions")

    return render(request, "home/user_info.html")

def validate_response(text):
    if not text:
        return False, "Empty response"

    words = text.strip().split()

    if len(words) < 5:
        return False, "Response too short"

    if not any(char.isalpha() for char in text):
        return False, "No meaningful text"

    return True, "Valid"

def questions(request):
    profession = request.session.get("profession")
    print("profession:--",profession)
    if not profession:
        return redirect("user_info")
    
    base_scenario = random.choice(SCENARIO_TEMPLATES[profession])
    print("base_scenario:--",base_scenario)
    categories = PROFESSION_CATEGORY_MAP.get(profession, [])
    questions = []

    for category in categories:
        question_text = random.choice(QUESTION_BANK[category])
        questions.append({
            "category": category,
            "question": question_text
        })

    return render(request, "home/questions.html", {
        "profession": profession,
        "scenario" : base_scenario,
        "questions": questions
    })

def submit_responses(request):
    if request.method == "POST":

        responses = request.POST.getlist("responses[]")
        categories = request.POST.getlist("categories[]")

        print("Responses:", responses)
        print("Categories:", categories)

        emotion_model = EmotionAnalyzer.load_model()

        category_scores_raw = {}
        emotional_details = []

        for response, category in zip(responses, categories):
            is_valid, _ = validate_response(response)
            if not is_valid:
                continue

            # Run emotion model
            model_output = emotion_model(response)[0]

            # Emotional breakdown
            breakdown = emotional_breakdown(model_output)
            emotional_details.append(breakdown)

            # EQ score
            eq_score = calculate_EQScore(category,breakdown)

            # Category aggregation
            category_scores_raw.setdefault(category, []).append(eq_score)


            emotional_details.append({
                "category": category,
                "breakdown": breakdown,
                "eq_score": round(eq_score)
            })

        # Aggregate category scores
        category_scores = aggregate_category_scores(category_scores_raw)

        # Overall EQ
        overall_eq, eq_level = calculate_overall_eq(category_scores)

        print("category_scores:--", category_scores)
        print("overall_eq:--", overall_eq)
        print("eq_level:--", eq_level)
        print("emotional_details:--",emotional_details)

        # plotting graphs
        categories = list(category_scores.keys())
        scores = list(category_scores.values())

        filename = f"{uuid.uuid4()}.png"
        folder = os.path.join(settings.MEDIA_ROOT, "eq_plots")
        os.makedirs(folder, exist_ok=True)

        file_path = os.path.join(folder, filename)

        plt.figure()
        plt.bar(categories, scores)
        plt.ylim(0, 100)
        plt.xlabel("EQ Categories")
        plt.ylabel("Score")
        plt.title("Category-wise Emotional Intelligence Scores")

        plt.tight_layout()
        plt.savefig(file_path)
        plt.close()
        plot_url = settings.MEDIA_URL + "eq_plots/" + filename

        return render(request, "home/results.html", {
            "category_scores": category_scores,
            "overall_eq": overall_eq,
            "eq_level": eq_level,
            "plot_url": plot_url,
        })

