# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget  # Import the widget
from .utils import GENDER_CHOICES


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "first name", "class": "form-control"}
        ),
        required=True,
        label="first name",
    )

    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "last name", "class": "form-control"}
        ),
        required=True,
        label="last",
    )

    email = forms.EmailField(
        max_length=100,
        help_text="Required. Enter a valid email address.",
        widget=forms.TextInput(attrs={"placeholder": "email", "class": "form-control"}),
        required=True,
        label="Email",
    )

    country = CountryField().formfield(
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label="Gender",
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
        label="Gender",
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "username", "class": "form-control"}
        ),
        required=True,
        max_length=50,
        label="Username",
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "password", "class": "form-control"}
        ),
        required=True,
        label="Password",
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "confirm password", "class": "form-control"}
        ),
        required=True,
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "country",
            "gender",
            "password1",
            "password2",
        ]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
        required=True,
        max_length=50,
        label="Username",
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
        required=True,
        label="Password",
    )

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {"country": CountrySelectWidget()}
