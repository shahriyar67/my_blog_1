from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Article, Category

# Register your models here.

def make_published(modeladmin, request, queryset):
    row_updated = queryset.update(status = 'p')
    if row_updated == 1 :
        massage_bit = "شد"
    else:
        massage_bit = "شدند"
    modeladmin.message_user(request,"{} مقاله منتشر {}"
                               .format(row_updated, massage_bit))
make_published.short_description = "منتشر شدن"

@admin.action(description='با دکوریتور پیش نویس شوند')
def make_drafted(modeladmin, request, queryset):
    row_updated = queryset.update(status = 'd')
    if row_updated == 1 :
        massage_bit = "شد"
    else:
        massage_bit = "شدند"
    modeladmin.message_user(request,"{} مقاله پیش نویس {}"
                               .format(row_updated, massage_bit))

def status_True(modeladmin, request, queryset):
    row_updated = queryset.update(status = True)
    if row_updated == 1 :
        massage_bit = "شد"
    else:
        massage_bit = "شدند"
    modeladmin.message_user(request,"{} دسته بندی منتشر {}"
                               .format(row_updated, massage_bit))
status_True.short_description = "منتشر شدن"

@admin.action(description='با دکوریتور پیش نویس شوند')
def statue_Fales(modeladmin, request, queryset):
    row_updated = queryset.update(status = False)
    if row_updated == 1 :
        massage_bit = "شد"
    else:
        massage_bit = "شدند"
    modeladmin.message_user(request,"{} دسته بندی پیش نویس {}"
                               .format(row_updated, massage_bit))


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'name', 'parent', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    actions = [statue_Fales, status_True]
    

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'author', 'slug','jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'publish', 'status')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_published, make_drafted]
    
    def category_to_str(self, obj):
        CatList = [i.name for i in obj.Category.published()]
        return ", ".join(CatList)
    category_to_str.short_description = "دسته بندی ها"



admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
