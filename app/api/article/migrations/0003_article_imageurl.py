# Generated by Django 3.2.4 on 2021-07-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_remove_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imageUrl',
            field=models.CharField(default='', max_length=120),
        ),
    ]