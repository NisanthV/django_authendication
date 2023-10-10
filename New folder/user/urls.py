
from django.contrib import admin
from django.urls import path
from user import views as v

urlpatterns = [
    path('',v.home),
    path('register/',v.register,name="reg"),
    path('login/',v.login,name="login"),


]
