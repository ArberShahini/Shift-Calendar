from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('activate/<str:token>', AccountActivationView.as_view()),
    path('reset/', PwdResetRequestView.as_view()),
    path('reset/<str:token>', PwdResetView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]