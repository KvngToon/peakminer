from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Deposit, Withdrawal, InvestmentPlan, Payments


class CustomUserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "balance")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "balance")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )


class DepositAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "created_at", "status", "investment_plan")
    list_filter = ("status", "investment_plan")
    search_fields = ("user__username", "user__email")


class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "created_at", "status")
    list_filter = ("status",)
    search_fields = ("user__username", "user__email")


class InvetsmentAdmin(admin.ModelAdmin):
    list_display = ("name", "duration", "interest_rate", "minimum_deposit")
    list_filter = ("name",)
    search_fields = ("name", "minimum_deposit")


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("payment_type", "wallet_address", "network_type")
    list_filter = ("payment_type",)
    search_fields = ("payment_type", "wallet_address", "network_type")


admin.site.register(Payments, PaymentsAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdrawal, WithdrawalAdmin)
admin.site.register(InvestmentPlan, InvetsmentAdmin)
admin.site.register(User, CustomUserAdmin)
