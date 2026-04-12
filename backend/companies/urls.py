from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CompanyRegisterView.as_view()),
    path('', CompanyGetAllView.as_view())
]