from django import forms
from .models import Contact, Portfolio
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['portfolio_name', 'portfolio_description', 'portfolio_image']


class LoginForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']