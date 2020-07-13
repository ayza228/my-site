from django.db import models
from django.urls import reverse


class Lesson(models.Model):
    title = models.TextField("Занятие", max_length=1000, blank=True)
    url = models.SlugField(max_length=130, unique=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("lesson_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Пробное занятие"
        verbose_name_plural = "Пробное занятие"


class Trial(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField()
    phone = models.TextField("Номер телефона", max_length=12)
    
    lesson = models.ForeignKey(
        Lesson, verbose_name="главное сообщение", blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.lesson}"

    class Meta:
        verbose_name = "Форма заполнения"
        verbose_name_plural = "Форма заполнения"

    