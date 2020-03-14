from django.shortcuts import render,redirect,reverse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username = form.cleaned_data['username']).exists():
                messages.warning(request, "User is already exists")
                return redirect(reverse('signup'))
            User.objects.create_user(**form.cleaned_data)
            messages.success(request, "You have successfully registered")
            return redirect(reverse('login_user'))
    form = SignUpForm()
    return render(request,'signup.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,username = form.cleaned_data['username'],password = form.cleaned_data['password'])
            if user:
                login(request,user)
                messages.success(request,'Successfully logged in')
                return redirect(reverse('profile'))
            else:
                messages.error(request,'Wrong email or password')
                return redirect(reverse('login_user'))
    form = LoginForm()
    return render(request,'login.html',{'form':form})


def logout_user(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect(reverse('login_user'))


def profile(request):
    username = request.user.username
    return render(request,'profile.html',{'username':username})