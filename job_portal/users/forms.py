from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','password1','password2']
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class WorkingRegisterForm(ModelForm):
    class Meta:
        model = WorkingUser
        fields = ['mobile','image','gender']
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        r = WorkingUser.objects.filter(mobile=mobile)
        if r.count():
            raise  ValidationError("mobile number already exists")
        return mobile

class RecruiterRegisterForm(ModelForm):
    class Meta:
        model = Recruiter
        fields = ['company_name','mobile','image','gender']
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        r = WorkingUser.objects.filter(mobile=mobile)
        if r.count():
            raise  ValidationError("mobile number already exists")
        return mobile

class AdminRegisterForm(ModelForm):
    class Meta:
        model = AdminUser
        fields = ['mobile','image','gender']
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        r = WorkingUser.objects.filter(mobile=mobile)
        if r.count():
            raise  ValidationError("mobile number already exists")
        return mobile

class WorkingUpdateForm(ModelForm):
    class Meta:
        model = WorkingUser
        fields = ['mobile','image']

class AdminUpdateForm(ModelForm):
    class Meta:
        model = AdminUser
        fields = ['mobile','image']

class RecruiterUpdateForm(ModelForm):
    class Meta:
        model = WorkingUser
        fields = ['mobile','image']


class UserUpdateForm(ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count()>1:
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count()>1:
            raise  ValidationError("Email already exists")
        return email

class RecruiterLoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password",max_length=20, widget=forms.PasswordInput)

class AdminLoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password",max_length=20, widget=forms.PasswordInput)

class NewsLetterUpload(ModelForm):
    class Meta:
        model = NewsLetterModel
        fields=['newsletter'] 