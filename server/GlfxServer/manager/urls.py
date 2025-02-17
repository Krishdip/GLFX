from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("register", RegisterView, basename="register_view")
router.register("accounts", AccountViewSet, basename="accounts_view")
router.register("tickets", SupportViewSet, basename="support")


urlpatterns = [
    path("token", CustomTokenObtain.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh_view"),
    path("session", TestSession.as_view()),
    # Profile Endpoints
    path("userinfo", UserInfoV.as_view()),
    path("personalinfo", PersonalInfoV.as_view(), name="personal_info"),
    path("financialinfo", FinancialInfoV.as_view(), name="financial_info"),
    path("security", SecurityUpdateV.as_view(), name="security_view"),
    # wallet endpoints
    path("wallet", WalletV.as_view(), name="wallet"),
    # Deposit / withdrawal endpoints
    path("management", TransactionCreateAPIView.as_view(),
         name="deposit_withdrawal"),
    path("transactions", TransactionV.as_view(), name="transactions_view"),
    # support
    path("newmessage", NewMessage.as_view(), name="new message"),
    path("reply", SendReply.as_view(), name="send reply"),
    # ViewSet Router
    path("", include(router.urls))
]
