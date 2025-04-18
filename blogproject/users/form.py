from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get("username")

        # Example: minimum 5 characters, alphanumeric only
        if not re.match(r'^[a-zA-Z0-9]+$', username):
            raise forms.ValidationError("Username must be alphanumeric only.")

        if len(username) < 5:
            raise forms.ValidationError("Username must be at least 5 characters long.")

        return username


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get("username")

        # Example: minimum 5 characters, alphanumeric only
        if not re.match(r'^[a-zA-Z0-9]+$', username):
            raise forms.ValidationError("Username must be alphanumeric only.")

        if len(username) < 5:
            raise forms.ValidationError("Username must be at least 5 characters long.")

        return username
