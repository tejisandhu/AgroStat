# Generated by Django 5.0.2 on 2024-02-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0018_agriculture_news_photographer"),
    ]

    operations = [
        migrations.AddField(
            model_name="agriculture_news",
            name="date",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="agriculture_news",
            name="sub_title",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
