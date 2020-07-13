from django.contrib import admin
from .models import Lesson, Trial

admin.site.register(Lesson)

@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
