from django.contrib import admin
from django.urls import path,include
from .views import*

urlpatterns = [
    path('',home,name=("home")),
    path('login',login,name=("login")),
    path('signup',signup,name=("signup")),
    path('logout',logout,name=("logout")),
    path('index', index,name=("index")),
    path('<int:id>/', Details,name=("Details")),
    path('<int:id>/add-comment', add_comment,name=("add_comment")),
]