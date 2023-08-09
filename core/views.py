from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/About.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


class SignupView(FormView):
    template_name = "core/signup.html"
    form_class = UserRegistrationForm
    success_url = "/login"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(LoginView):
    template_name = "core/login.html"
    form_class = UserLoginForm

    def get_success_url(self) -> str:
        return reverse_lazy("index")
