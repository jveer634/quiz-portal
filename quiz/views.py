from django.shortcuts import render

def list_view(request):
	quizzes = Quiz.objects.filer()