# Generated by Django 4.2.6 on 2023-12-04 03:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("salon", "0004_bookings"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookings",
            old_name="user",
            new_name="User",
        ),
    ]
