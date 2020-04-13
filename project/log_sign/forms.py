from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import normal_user

class normal_user_form(UserCreationForm):

    student_number = forms.CharField(required=False)
    phone = forms.CharField(required=False)


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'student_number', 'phone']