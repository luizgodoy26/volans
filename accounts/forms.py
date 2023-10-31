from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from companies.models import Company

from django.utils.safestring import mark_safe

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    full_name = forms.CharField(label='Nome completo',  widget=forms.TextInput)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'seller', 'manager', 'company')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas precisam ser iguais")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        labels = {
            'full_name': ('Nome completo'),
            'email': ('Email'),
            'password': ('Senha'),
        }
        fields = ('email', 'full_name', 'password', 'seller', 'manager', 'company')

    def clean_password(self):
        return self.initial["password"]



class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is None:
            raise forms.ValidationError("Credenciais inválidas")
        login(request, user)
        self.user = user
        return data


class RegisterForm(forms.ModelForm):
    full_name = forms.CharField(required=True, label='Nome completo', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Seu nome aqui'}))
    email = forms.CharField(required=True, label='E-mail', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Seu email aqui'}))
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Sua senha aqui'}))
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}))
    seller = forms.BooleanField()
    manager = forms.BooleanField()

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'seller', 'manager', 'company')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas precisam ser iguais")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def __init__(self,  *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['company_client'].queryset = Company.objects.filter(user=self.user)
