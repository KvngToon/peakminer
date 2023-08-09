# Generated by Django 4.2.3 on 2023-07-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_remove_user_gender_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
                max_length=10,
            ),
        ),
    ]
