from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Article



class ArticleView(ListView):
    """Список статей"""
    model = Article
    queryset = Article.objects.all()
    template_name = "articles/articles_list"



class ArticleDetailView(DetailView):
    """Полное описание статьи"""
    model = Article
    slug_field = "url"