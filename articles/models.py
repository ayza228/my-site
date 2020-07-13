from django.db import models
from datetime import date
from django.urls import reverse



class Article(models.Model):
    title = models.CharField("Название", max_length=120)
    post = models.TextField("Содержание статьи")
    date = models.DateTimeField("Дата публикации")
    poster = models.ImageField("Постер", upload_to="articles/")
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"