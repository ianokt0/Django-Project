# Generated by Django 5.0.1 on 2024-01-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='berita', max_length=50),
        ),
    ]