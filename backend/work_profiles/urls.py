from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateWorkProfileView.as_view()),
    path('getByCompanyId/<int:company_id>', getWorkProfileByIdView.as_view())
]