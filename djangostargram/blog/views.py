from django.shortcuts import render, redirect
from .models import Dsuser
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.core.paginator import Paginator

# Create your views here.

def timeline(request):
    user = Dsuser.objects.filter(id=request.user.id).first()
    email = user.email if user else "Anonymous User!"
    print(email)
    print(request.user.is_authenticated)
    msg = f"Hello! {user}"

    page = int(request.GET.get("p", 1))
    posts = Post.objects.all().order_by("-created_date")
    paginator = Paginator(posts, 4)
    posts = paginator.get_page(page)

    if request.user.is_authenticated is False:
        email = "Anonymous User!"
        print(email)
        msg = "Hello! Anonymous User!"
    return render(request, "timeline.html", {"msg": msg, "posts": posts})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터입니다."
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            conf_password = form.cleaned_data.get("password2")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입완료"
            return redirect("timeline")
        return render(request, "register.html", {"form": form, "msg": msg})
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        msg = "가입되어 있지 않거나 로그인 정보가 잘못 되엇습니다."
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                msg = "로그인 성공"
                login(request, user)
                return redirect("timeline")
        return render(request, "login.html", {"form": form, "msg": msg})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

def logout_view(request):
    auth.logout(request)
    return redirect("timeline")

def upload(request):
    return render(request, "upload.html", {})