from django.urls import path
from .views import *

urlpatterns = [
    path('register',register_customer,name='register'),
    path('login',login_customer,name='login'),
    path('logout',logout_customer,name='logout'),
]
