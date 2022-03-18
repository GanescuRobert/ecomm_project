from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    classStyle = 'form-control my-2'
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': classStyle, 'placeholder': "Enter username"}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': classStyle, 'placeholder': "Enter email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': classStyle, 'placeholder': "Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': classStyle, 'placeholder': "Confirm password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
