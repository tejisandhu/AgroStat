# Generated by Django 5.0.2 on 2024-05-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0032_dealers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dealers",
            name="image",
            field=models.ImageField(blank=True, upload_to="Dealers"),
        ),
    ]
