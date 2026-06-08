from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Korisničko ime'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Lozinka'
        self.fields['password2'].label = 'Potvrda lozinke'
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'auth-input')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Korisničko ime'
        self.fields['password'].label = 'Lozinka'
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'auth-input')
