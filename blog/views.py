from django.shortcuts import render
from .models import Article
# Create your views here.

def home(request):
    context = {
        "article":Article.objects.filter(status="p").order_by('-publish')
    }
    return render(request,'blog/home.html',context)

def detail(request,slug):
    context = {
        "article":Article.objects.get(slug = slug)
    }
    return render(request,"blog/detail.html",context)