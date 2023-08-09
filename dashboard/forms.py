from django import forms
from core.models import Deposit, InvestmentPlan, Withdrawal, User
from django_countries.widgets import CountrySelectWidget  # Import the widget
from core.utils import GENDER_CHOICES
from django_countries.fields import CountryField


class DepositForm(forms.ModelForm):
    amount = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter amount", "class": "form-control px-2"}
        ),
        label="Amount",  # Change the label to "Amount"
    )

    investment_plan = forms.ModelChoiceField(
        queryset=InvestmentPlan.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Investment Plan",
        empty_label=None,  # Remove the default '---------' option
    )

    class Meta:
        model = Deposit
        fields = ["amount", "investment_plan"]


class WithdrawalForm(forms.ModelForm):
    amount = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter amount", "class": "form-control px-2"}
        ),
        label="Amount",  # Change the label to "Amount"
    )

    wallet = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter Wallet", "class": "form-control px-2"}
        ),
        label="Amount",  # Change the label to "Amount"
    )

    crypto_network = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter Crypto Network", "class": "form-control px-2"}
        ),
        label="Amount",  # Change the label to "Amount"
    )

    class Meta:
        model = Withdrawal
        fields = ["amount", "wallet", "crypto_network"]


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control px-2"}),
        required=True,
        label="first name",
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control px-2"}),
        required=True,
        label="last",
    )

    email = forms.EmailField(
        max_length=100,
        help_text="Required. Enter a valid email address.",
        widget=forms.TextInput(attrs={"class": "form-control px-2"}),
        required=True,
        label="Email",
    )

    country = CountryField().formfield(
        widget=forms.Select(attrs={"class": "form-control px-2"}),
        required=True,
        label="Gender",
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-control px-2"}),
        required=True,
        label="Gender",
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "country", "gender"]
