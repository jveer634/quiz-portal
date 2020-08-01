from django.urls import path
from quiz.views import list_view

app_name = "quiz"

urlpatterns = [
	path('', list_view, name="quiz_list"),
]
