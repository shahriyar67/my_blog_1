from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="نام دسته بندی")
    position = models.IntegerField(verbose_name="پوزیشن")
    status = models.BooleanField(default=True, verbose_name="منتشر شود؟")
    slug = models.SlugField(default='', max_length=100, unique=True,
                             verbose_name="اسلاگ دسته بندی")
    
    class Meta:
        ordering = ['position']
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیشنویس'),
        ('p', 'منتشر شده'),
    )
    author = models.CharField(max_length=50, verbose_name="گردآوری شده توسط")
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True,
                            verbose_name="آدرس مقاله")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر")
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name="زمان انتشار")
    Category = models.ManyToManyField(Category)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              verbose_name="وضعیت")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish', 'status']
    
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"
