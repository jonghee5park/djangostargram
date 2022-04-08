from django import forms
from django.contrib.auth.forms import UserCreationForm
from blog.models import Dsuser, Post

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)

    class Meta:
        model = Dsuser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

class PostForm(forms.modelForm):
    imgsrc = forms.CharField(max_length=200)
    contents = forms.TextField()
    tags = forms.ManytoMany

    class Meta:
        model = Post