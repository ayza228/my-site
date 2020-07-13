
from django.urls import path, include
from . import views

urlpatterns = [
    path("about/", views.about, name='about'),
    path("mentalarithm/", views.mentalarithm, name='mentalarithm'),
    path("speedreading/", views.speedreading, name='speedreading'),
    path("reading/", views.reading, name='reading'),
    path("calligraphy/", views.calligraphy, name='calligraphy'),
    path("main/", views.LessonView.as_view()),
    path("<slug:slug>/", views.LessonDetailView.as_view(), name="lesson_detail"),
    path("trial/<int:pk>/", views.AddTrial.as_view(), name='add_trial'),
]
