from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Lesson, Trial
from .forms import TrialForm


    
def about(request):
    return render(request, 'articles/about.html')

def mentalarithm(request):
    return render(request, 'articles/mentalarithm.html')

def speedreading(request):
    return render(request, 'articles/speedreading.html')

def reading(request):
    return render(request, 'articles/reading.html')

def calligraphy(request):
    return render(request, 'articles/calligraphy.html')

def triallesson(request):
    return render(request, 'articles/triallesson.html')



class LessonView(View):
    def get(self, request):
        lessons = Lesson.objects.all()
        return render(request, "articles/mainpage.html", {"lesson_list": lessons})



class LessonDetailView(View):
    def get(self, request, slug):
        lesson = Lesson.objects.get(url=slug)
        return render(request, "articles/lesson_detail.html", {"lesson": lesson})



class AddTrial(View):
    def post(self, request, pk):
        form = TrialForm(request.POST)
        lesson = Lesson.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.lesson = lesson
            form.save()
        return redirect("/main")
