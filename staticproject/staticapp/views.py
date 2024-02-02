from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import place
from .models import travelspots
# Create your views here.
def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=uname,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
             messages.info(request,"Invalid Credential")
             return redirect('login')
    return render(request,"login1.html")
def index(request):
    obj=place.objects.all()
    obj1=travelspots.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']

        email= request.POST['email']
        pass1=request.POST['password']
        cpass = request.POST['confirmpassword']
        if pass1==cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
                user.save();
                return redirect('login')


        else:
            messages.info(request,"Password not Match")
            return redirect('register')
        return redirect('/')
    return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')



