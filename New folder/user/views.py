from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm as us
from user.forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
import time


def home(req):
    return render(req,'base1.html')
def register(req):
    if req.method=='POST':
       name=req.POST['username']
       email=req.POST['email']
       password1=req.POST['password1']
       password2=req.POST['password2']
       if password2==password1:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.save()
            messages.success(req,"success")
            time.sleep(3)
            return redirect('login')
       else:
            messages.warning(req,"missmatch password")
            time.sleep(3)
            return redirect('reg')
    else:
        form=CreateUserForm()
        return render(req,'register/register.html',{"form":form})
def login(req):
    return render(req,'login.html')