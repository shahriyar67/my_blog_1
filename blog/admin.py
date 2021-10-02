from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Article,Category

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'jpublish', 'status')
    list_filter = ('author', 'publish', 'status')
    search_fields = ('author', 'publish', 'status')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'publish')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)