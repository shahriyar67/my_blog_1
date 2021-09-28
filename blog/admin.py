from django.contrib import admin
from .models  import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','jpublish','jcreated','status')
    list_filter = ('author','publish','status','created')
    search_fields = ('author','publish','status')
    prepopulated_fields={'slug':('title'[:10],)}

admin.site.register(Article,ArticleAdmin)