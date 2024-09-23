from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError
from django.http import Http404

from django.db.models import Q 


def base(req):
    return render(req,"base.html")
@login_required
def jobfeedpage(req):
    return render(req,"jobfeedpage.html")


def loginPage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        if not username or not password:
            messages.warning(req, "Both username and password are required")
            return render(req, "loginPage.html")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)
            messages.success(req, "Login Successfully")
            return redirect("jobfeedpage")
        else:
            messages.warning(req, "Invalid username or password")

    return render(req, "loginPage.html")

def register(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        usertype=req.POST.get('usertype')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')
        if not all([username,usertype,password,confirm_password]):
            messages.warning(req, "All fields are requierd.")
                
            return render(req,'register.html')

        if password != confirm_password:
            messages.warning(req, "password do not matched.")   
            return render(req,'register.html')

          
        if len (password)<8:
            messages.warning(req, "password must be at least 8  character .")  
            return render(req,'register.html')
        

        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            messages.warning(req, "Password must contain both letters and numbers")
            return render(req,'register.html')
           
        try:
            user = CUSTOM_USER.objects.create_user(
                username=username,
                email=email,
                usertype=usertype,
                password=password
            )
            messages.success(req, "Account created successfully! Please log in.")
            return redirect("loginPage")
        except IntegrityError:
            messages.warning(req, "Username or email already exists")
            return render(req, "register.html")

    return render(req, "register.html")

        
    



def logoutPage(req):
    logout(req)
    messages.success(req, "you have logged out successfully")
    return redirect('loginPage')




