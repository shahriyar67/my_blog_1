from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.views.generic import ListView, DetailView

class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 4

#def detail(request, slug):
#    context = {
#        "article": get_object_or_404(Article, slug=slug, status="p"),
#        
#    }
#    return render(request, "blog/detail.html", context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(),slug= slug)


#def category(request, slug, page=1):
#    category = get_object_or_404(Category, slug=slug, status=True)
#    article_list = category.articles.published()
#    paginator = Paginator(article_list, 4)
#    articles = paginator.get_page(page)
#    context = {
#        "category": category,
#        "articles": articles
#    }
#    return render(request, 'blog/category.html', context)
#

class CategoryList(ListView):
    paginate_by = 5
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        global category
        category = get_object_or_404(
            Category.objects.published(),slug= slug)
        return category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context