from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="نام دسته بندی")
    position = models.IntegerField(verbose_name="پوزیشن")
    publish = models.BooleanField(verbose_name="منتشر شود؟")
    
    class Meta:
        ordering = ['position']


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
    category = models.ManyToManyField(Category)
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
    
    def jcreated(self):
        return jalali_converter(self.created)
    jcreated.short_description = "زمان ساخته شدن مقاله"