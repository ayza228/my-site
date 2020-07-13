from django.db import models
from datetime import date
from django.urls import reverse


class Movie(models.Model):
    title = models.TextField("Главное", max_length=2000)
    poster = models.ImageField("Постер", upload_to="reviews/")
    url = models.SlugField(max_length=130, unique=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Главное"
        verbose_name_plural = "Главное"



class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    movie = models.ForeignKey(
        Movie, verbose_name="главное сообщение", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"