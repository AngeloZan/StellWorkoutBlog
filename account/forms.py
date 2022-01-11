# This is not actually my code
# You can check https://www.youtube.com/playlist?list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW
# I used this course to build my account app

from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate
import datetime

from account.models import Account, Profile

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RegistrationForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(max_length=60, help_text="Obrigatório, informe um endereço de e-mail válido.")

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')
        error_messages = {
            'username': {
                'unique': 'Este nome de usuário não está disponível.',
            },
        }

class AccountAuthenticationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': 'autofocus', 'required': 'required'})

    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Login inválido")


class AccountUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(AccountUpdateForm, self).__init__(*args, **kwargs)
    
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            },
            format='%Y-%m-%d'
            ),
        input_formats=['%Y-%m-%d'],
        label='Nascimento',
        required=False
    )

    class Meta:
        model = Account
        fields = ['username', 'name', 'email', 'date_of_birth', 'country', 'gender']
        error_messages = {
            'username': {
                'unique': 'Este nome de usuário não está disponível.',
            },
        }

class PasswordChangeFormCustom(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PasswordChangeFormCustom, self).__init__(*args, **kwargs)
