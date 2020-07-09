from django.forms import ModelForm
from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)
	password = forms.CharField(max_length=30,widget=forms.PasswordInput)
	confirm_password = forms.CharField(max_length=30,widget=forms.PasswordInput)
