# Generated by Django 4.0.1 on 2022-01-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_category_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(default='', null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]