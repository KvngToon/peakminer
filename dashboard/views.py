from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from core.models import InvestmentPlan, User, Withdrawal, Deposit, Payments
from django.db.models import Sum, Count
from .forms import DepositForm, WithdrawalForm, UserProfileForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        withdrawals = Withdrawal.objects.filter(user=self.request.user)
        withdrawal_total = Withdrawal.objects.filter(
            user=self.request.user, status="Approved"
        ).aggregate(Sum("amount"))["amount__sum"]
        deposit_total = Deposit.objects.filter(
            user=self.request.user, status="Approved"
        ).aggregate(Sum("amount"))["amount__sum"]
        investments_count = Deposit.objects.filter(
            user=self.request.user, status="Approved"
        ).aggregate(Count("investment_plan"))["investment_plan__count"]
        investments = InvestmentPlan.objects.all()

        context["withdrawals"] = withdrawals
        context["withdrawals_total"] = withdrawal_total
        context["deposit_total"] = deposit_total
        context["investments_count"] = investments_count
        context["investments"] = investments

        return context


class InvestmentView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/investments.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        deposit = Deposit.objects.filter(user=self.request.user)
        context["deposit"] = deposit
        return context


class DepositView(LoginRequiredMixin, FormView):
    template_name = "dashboard/deposits.html"
    form_class = DepositForm
    success_url = reverse_lazy("deposits")

    def form_valid(self, form):
        # Process the form data when it's valid
        form.instance.user = self.request.user
        form.save()  # Save the form data to the database
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["deposit"] = Deposit.objects.filter(user=self.request.user)
        context["payments"] = Payments.objects.all()
        return context


class WithdrawalView(LoginRequiredMixin, FormView):
    template_name = "dashboard/withdrawal.html"
    form_class = WithdrawalForm
    success_url = reverse_lazy("withdrawal")

    def form_valid(self, form):
        user_balance = self.request.user.balance
        withdrawal_amount = int(form.cleaned_data["amount"])

        if user_balance >= withdrawal_amount:
            form.instance.user = self.request.user
            form.save()
            return super().form_valid(form)
        else:
            return render(
                self.request,
                self.template_name,
                {
                    "form": form,
                    "error_message": "Insufficient balance for withdrawal.",
                    "withdrawals": Withdrawal.objects.filter(user=self.request.user),
                },
            )

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["withdrawals"] = Withdrawal.objects.filter(user=self.request.user)
        return context


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "dashboard/profile.html"
    form_class = UserProfileForm
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserProfileForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect(reverse_lazy("profile"))
    else:
        user_form = UserProfileForm(instance=request.user)
    return render(
        request,
        "dashboard/profile.html",
        {"form": user_form},
    )


def logoutview(request):
    logout(request)
    return redirect(reverse_lazy("home"))
