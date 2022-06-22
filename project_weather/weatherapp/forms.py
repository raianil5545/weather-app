from django import forms
from .models import AppUser


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        # to generate form with all fields/ attributes
        # fields = "__all__"

        # to generate form with limited/ custom fields
        fields = ('email', 'password')

        model = AppUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('first_name', 'middle_name', 'last_name', \
                  'email', 'contact', 'dob', 'password', 'address')

        model = AppUser
