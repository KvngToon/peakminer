# Generated by Django 4.2.3 on 2023-07-31 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_alter_user_gender"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "wallet_address",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "network_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
            ],
        ),
        migrations.AddField(
            model_name="deposit",
            name="completion_percentage",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="withdrawal",
            name="crypto_network",
            field=models.CharField(default="ETH", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="withdrawal",
            name="wallet",
            field=models.CharField(default="balablue", max_length=200),
            preserve_default=False,
        ),
    ]
