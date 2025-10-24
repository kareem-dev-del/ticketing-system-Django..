from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']