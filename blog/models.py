from django.db import models
#from django.db.models.deletion import SET_NULL
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html
from account.models import User
from django.urls import reverse

# my managers


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def published(self):
        return self.filter(status=True)
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="نام دسته بندی")
    parent = models.ForeignKey('self', null=True, blank=True, default=None,
                               on_delete=models.SET_NULL,
                               related_name='children', verbose_name='زیر دسته')
    position = models.IntegerField(verbose_name="پوزیشن")
    status = models.BooleanField(default=True, verbose_name="منتشر شود؟")
    slug = models.SlugField(max_length=100, unique=True,
                            verbose_name="اسلاگ دسته بندی")
    
    class Meta:
        ordering = ['parent__id', 'position']
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name
    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیشنویس'),
        ('p', 'منتشر شده'),
        ('i', 'درحال بررسی'),
        ('b', 'برگشت داده شده'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True,
                            verbose_name="آدرس مقاله")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر")
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name="زمان انتشار")
    Category = models.ManyToManyField(Category, related_name="articles")
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              verbose_name="وضعیت")
    is_special = models.BooleanField(default= False, verbose_name= "مقاله ویژه")
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish', 'status']
    
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"
    
    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
    
    def get_absolute_url(self):
        return reverse("account:home")
    
    def category_to_str(self):
        CatList = [i.name for i in self.Category.published()]
        return ", ".join(CatList)
    category_to_str.short_description = "دسته بندی ها"
        
    objects = ArticleManager()