from multiprocessing import context
from django.shortcuts import render, redirect
from datetime import datetime
from shiv.models import Wallq
from shiv.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Wallqna(request):
    if request.method == "POST":
        hash = request.POST.get('hashtag')
        ques = request.POST.get('question')
        print(ques)
        Qna = Wallq(hashtag=hash,question=ques)
        Qna.save()
        messages.success(request, 'Thank you! Your Question has been recorded.')
    qna_list = Wallq.objects.all().order_by('serial')   #to fetch all the table data
    return render(request, 'content/wallqa.html', {'qna_ins': qna_list})

def Vision(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Thank you! Your Message has been received.')
    return render(request, 'home/vision.html')

def LoginUser(request):

    if request.method == 'GET':
        username = request.GET.get('siname')
        password = request.GET.get('sipass')
        #check if user has entered correct credentials
        user = authenticate(username=username,password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user) 
            return redirect("/blog")
        else:
            return render(request, 'home/login.html')
            # No backend authnticated the credentials

    elif request.method == 'POST':
         username = request.POST.get('suname')
         email = request.POST.get('suemail')
         password = request.POST.get('supass')
         user = User.objects.create_user(username=username,email=email,password=password)
         user.save()
    
    

    return render(request, 'home/login.html')


def Analytics(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request, 'home/profile.html')

def Setting(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        # if request.method == "POST":
        #     username = request.POST.get('username')
        #     Firstname = request.POST.get('FirstName')
        #     Lastname = request.POST.get('LastName')
        #     User1 = User.objects.get(request.user)
        #     user = User1(username=username,first_name=Firstname,last_name=Lastname)
        #     user.save()
        #     messages.success(request, 'Yout Profile has been updated.')
        return render(request, 'home/setting.html')
    
    

def LogoutUser(request):
    logout(request)
    return redirect("/")

