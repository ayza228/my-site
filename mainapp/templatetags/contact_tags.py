from django import template
from mainapp.forms import TrialForm

register = template.Library()


@register.inclusion_tag("articles/form.html")
def contact_form():
    return {"contact_form": TrialForm() }