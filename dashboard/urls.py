from django.urls import path
from .views import (
    IndexView,
    InvestmentView,
    DepositView,
    WithdrawalView,
    ProfileView,
    logoutview,
    profile,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("investments", InvestmentView.as_view(), name="investments"),
    path("deposits", DepositView.as_view(), name="deposits"),
    path("withdrawal", WithdrawalView.as_view(), name="withdrawal"),
    path("profile", profile, name="profile"),
    path("logout", logoutview, name="logout"),
]
