from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from blog.models import Article
from django.urls import reverse_lazy
from .mixins import (
    FieldMixins,
    FormValidMixin,
    AuthorAccessMixin,
    AuthorsAccessMixin,
    SuperUserAccessMixin
)
from django.shortcuts import get_object_or_404
from .models import User
from .forms import ProfileForm
from django.contrib.auth.views import LoginView
# Create your views here.

class ArticleList(LoginRequiredMixin, AuthorsAccessMixin, ListView):
    template_name = "registration/home.html"
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, AuthorsAccessMixin, FormValidMixin, FieldMixins, CreateView):
    model = Article
    template_name = 'registration/Article_create_update.html'
    

class ArticleUpdate(AuthorAccessMixin, AuthorsAccessMixin, FormValidMixin, FieldMixins, UpdateView):
    model = Article
    template_name = 'registration/Article_create_update.html'
    

class ArticleDelete(SuperUserAccessMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('account:home')
    template_name = 'registration/article_delete.html'


class ArticlePreview(AuthorsAccessMixin, DeleteView):
    def get_object(self) :
        pk = self.kwargs.get('pk')
        return get_object_or_404 (Article,pk=pk)
    template_name = 'registration/article_confirm_delete.html'


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('account:profile')
    form_class = ProfileForm
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    
    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy("account:home")
        else :
            return reverse_lazy("account:profile")
