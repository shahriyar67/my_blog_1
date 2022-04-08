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
    return {
        "category": Category.objects.filter(status=True)
    }

@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link": "account:{}".format(link_name),
        "content": content,
        "classes": classes,
    }