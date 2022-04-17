from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


class CustomRegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'name' : "username", 'type':"username", 'placeholder':"Username"}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input', 'name':"password1", 'type':"password", 'placeholder':"Password"}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input', 'name':"password2", 'type':"password", 'placeholder':"Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CustomLoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'name': "username", 'type': "username", 'placeholder': "Username"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input', 'name': "password", 'type': "password", 'placeholder': "Password"}))
