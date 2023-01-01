from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('CustomerSignUp', views.CustomerSignUp),
    path('StaffSignUp', views.StaffSingUp),
]
