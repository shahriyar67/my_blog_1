from django import template
from ..models import Category
from django.template.loader import get_template

register = template.Library()


@register.simple_tag
def tags():
    return Category.name


templateAdress = get_template("blog/partials/category_navbar.html")


@register.inclusion_tag(templateAdress)
def category_navbar():
    return{
        "category": Category.objects.filter(status=True)
    }
