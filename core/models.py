from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from .utils import GENDER_CHOICES, STATUS_CHOICES


# TODO:
# ADD WALLET MODEL TO STORE PAYMENT WALLETS --  Done


class User(AbstractUser):
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    country = CountryField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # Add custom related names for many-to-many relationships
    groups = models.ManyToManyField(
        "auth.Group", related_name="custom_user_set", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="custom_user_set", blank=True
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["balance"]


class InvestmentPlan(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_deposit = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["minimum_deposit"]


class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][1]
    )
    investment_plan = models.ForeignKey(
        InvestmentPlan, on_delete=models.CASCADE, related_name="deposits"
    )
    completion_percentage = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.amount} ({self.investment_plan.name})"

    class Meta:
        ordering = ["-created_at"]


class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][1]
    )
    wallet = models.CharField(max_length=200)
    crypto_network = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"

    class Meta:
        ordering = ["-created_at"]


class Payments(models.Model):
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    wallet_address = models.CharField(max_length=50, blank=True, null=True)
    network_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.payment_type}"

    class Meta:
        ordering = ["payment_type"]
