# Generated by Django 5.0.1 on 2024-01-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]