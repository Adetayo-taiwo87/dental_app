from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1','password2']

class LoginForm(AuthenticationForm):
        username = forms.CharField(label='username')
        password = forms.CharField(widget=forms.PasswordInput)


