from django.contrib import admin
from .models import Movie, Reviews

admin.site.register(Movie)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "text")
