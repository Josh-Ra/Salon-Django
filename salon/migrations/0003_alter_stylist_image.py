# Generated by Django 4.2.6 on 2023-12-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salon", "0002_stylist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stylist",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]