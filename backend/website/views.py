from email import message
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    #checking if a person is logging in
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        #authnetication
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Welcome Back")
            return redirect('home')
        else:
            messages.success(request,"Sorry, you must have mis-spelled your username or password")
            return redirect('home')
    else:
        return render(request,'home.html', {})



def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out")
    return redirect('home')

def register_user(request):
    return render(request,'register.html', {})

