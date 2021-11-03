from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Article, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'name', 'parent', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'jpublish', 'status', 'category_to_str')
    list_filter = ('author', 'publish', 'status')
    search_fields = ('title', 'author', 'publish', 'status')
    prepopulated_fields = {'slug': ('title',)}
    
    def category_to_str(self, obj):
        CatList = [i.name for i in obj.Category.published()]
        return ", ".join(CatList)
    category_to_str.short_description = "دسته بندی ها"



admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
