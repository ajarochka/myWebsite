from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    subject = forms.CharField(label='Email subject',
                               widget=forms.TextInput(attrs={'class': 'form_control', 'autocomplete': 'off'}))
    content = forms.CharField(label='Message body',
                               widget=forms.Textarea(attrs={'class': 'form_control', "rows": 10}))

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User name',
                               widget=forms.TextInput(attrs={'class': 'form_control', 'autofocus': 'None'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_control'}))



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form_control', 'autofocus': 'None'}))
    email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control', "autocomplete": 'off'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form_control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form_control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form_control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form_control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form_control'}),
        # }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'category', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_control'}),
            'content': forms.Textarea(attrs={'class': 'form_control', 'rows': 20}),
            'category': forms.Select(attrs={'class': 'form_control'}),
            # 'car_brand': forms.Select(attrs={'class': 'form_control'}),
            'photo': forms.FileInput(attrs={'class': 'form_control'}),
        }

# title = forms.CharField(max_length=150, label='Название новости ',
#                         widget=forms.TextInput(attrs={"class": "form-control"}))
# content = forms.CharField(label='Текст ', required=False,
#                           widget=forms.Textarea(attrs={"class": "form-control",
#                                                        "rows": 20})  )
# is_published = forms.BooleanField(label='Опубликовано? ', initial=True)
# category = forms.ModelChoiceField(empty_label='Выберите новость',label='Категория ',
#                                   queryset = Category.objects.all(),
#                                   widget=forms.Select(attrs={"class": "form-control"}))
