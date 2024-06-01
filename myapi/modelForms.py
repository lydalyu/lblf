from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class LoginForm(forms.Form):
    class Meta:
        fields = ['email', 'password']
    email = forms.CharField(max_length=100, label="Email", widget=forms.TextInput(attrs={'required' : True, 'placeholder' : 'Email', 'type' : 'email'}))
    password = forms.CharField(max_length=100, label="Password", widget=forms.TextInput(attrs={'required' : True, 'placeholder' : 'Password', 'type' : 'password'}))


class RegisterForm(forms.Form):
    class Meta:
        fields = ['email', 'password', 'password_confirm']
    email = forms.CharField(max_length=100, label="Email", widget=forms.TextInput(attrs={'required' : True, 'placeholder' : 'Email', 'type' : 'email'}))
    password = forms.CharField(max_length=100, label="Password", widget=forms.TextInput(attrs={'required' : True, 'placeholder' : 'Password', 'type' : 'password'}))
    password_confirm = forms.CharField(max_length=100, label="Password confirmation", widget=forms.TextInput(attrs={'required' : True, 'placeholder' : 'Password confirmation', 'type' : 'password'}))