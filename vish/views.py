from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def Community(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
#         return redirect("/login")   redirect needs to be imported
    return render(request, 'Community/join.html')