# Generated by Django 4.2.3 on 2023-08-02 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_alter_deposit_completion_percentage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deposit",
            name="investment_plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="deposits",
                to="core.investmentplan",
            ),
        ),
    ]
