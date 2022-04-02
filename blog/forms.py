from django import forms
from .models import Contact

from django.contrib.auth.models import User  # New
from django.contrib.auth.forms import UserCreationForm  # New


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'subject',
            'email',
            'sender',
            'detail'
        ]


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    model = User
    fields = [
        'username',
        'email',
        'password1',
        'password2'
    ]




