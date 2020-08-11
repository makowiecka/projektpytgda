from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from user.models import User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class LoginForm(AuthenticationForm):
    username = UsernameField(
        label = False,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika', 'class': 'form-control form-control-lg pr-4 shadow-none'}) #typ pola okreslony widgetem
    )

    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło', 'class': 'form-control form-control-lg pr-4 shadow-none' })
    )

    error_messages = {
        'invalid_login': 'Nieprawidłowe hasło lub login',
        'inactive': 'Konto nieaktywne'
    }