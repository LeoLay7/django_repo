# Generated by Django 4.0.5 on 2022-08-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
