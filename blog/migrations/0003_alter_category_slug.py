# Generated by Django 3.2.4 on 2021-10-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211016_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ دسته بندی'),
        ),
    ]