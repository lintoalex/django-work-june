from django import forms

from django.contrib.auth.forms import UserCreationForm

from todo.models import User,Todo


class SignUpForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    class Meta:

        model=User

        fields=["username","email","password1","password2","phone"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "email":forms.EmailInput(attrs={"class":"form-control mb-3"}),
            "phone":forms.NumberInput(attrs={"class":"form-control mb-3"})
        }

class SignInForm(forms.Form):

    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))

class TodoForm(forms.ModelForm):

    class Meta:

        model=Todo

        fields=["title"]

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control mb-3"})
        }