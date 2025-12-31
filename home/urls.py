from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_info, name="user_info"),
    path("questions/", views.questions, name="questions"),
    path("submit/", views.submit_responses, name="submit_responses"),
]
