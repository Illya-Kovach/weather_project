from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Паролі не співпадають")
        return password2

    def clean(self):
        cleaned_data = super().clean()
        if not all(cleaned_data.get(field) for field in self.fields):
            raise ValidationError("Всі поля обов'язкові")
        return cleaned_data


from django import forms
from .models import SearchHistory

class SearchHistoryForm(forms.ModelForm):
    class Meta:
        model = SearchHistory
        fields = ['city', 'temperature', 'description', 'user']

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Нікнейм'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
        required=True
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Користувач з таким ім'ям не знайдений.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise forms.ValidationError("Пароль має бути не менше 6 символів.")
        return password


