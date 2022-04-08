from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from blog.models import Article
from django.urls import reverse_lazy
from .mixins import FieldMixins, FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin
from django.shortcuts import get_object_or_404
# Create your views here.

class ArticleList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FormValidMixin, FieldMixins, CreateView):
    model = Article
    template_name = 'registration/Article_create_update.html'
    

class ArticleUpdate(AuthorAccessMixin, FormValidMixin, FieldMixins, UpdateView):
    model = Article
    template_name = 'registration/Article_create_update.html'
    

class ArticleDelete(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = 'registration/article_delete.html'


class ArticlePreview(LoginRequiredMixin, DeleteView):
    def get_object(self) :
        pk = self.kwargs.get('pk')
        return get_object_or_404 (Article,pk=pk)
    template_name = 'registration/article_confirm_delete.html'
    