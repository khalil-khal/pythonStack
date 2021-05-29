from django.http.request import HttpRequest
from django.shortcuts import render,redirect
from . import models
import re
from django.contrib import messages
import bcrypt
from .models import *


def index(request):
    return render(request,"index.html")

def registration(request):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors={}
    if len(request.POST['fname'])<2:
        errors['fname']='first name is too short' #بنادي على الفيرست نيم عن طريق النيم الي بال اتش تي ام ال
        

    if len(request.POST['fname'])<2:
        errors['lname']='last name is too short'
        

    if EMAIL_REGEX.match(request.POST['email']):
        errors['email']="invalid email address"
        

    if len(request.POST['password'])<8:
        errors['password']='short password'
        

    if request.POST["password"] != request.POST["confirm"]:
        errors['confirm']='Not matching'
        


    for key,value in errors.items():
        if len(errors)>0:
            messages.error(request,value)
    
    else :
        first=request.POST["fname"]
        last=request.POST["lname"]
        em=request.POST["email"]
        pas=request.POST["password"]
        conf=request.POST["confirm"]
        if pas == conf :
            hash =  bcrypt.hashpw(pas.encode(), bcrypt.gensalt()).decode()
            User .objects.create(first_name=first,last_name=last,email=em,password=hash)
            if 'name' not in request.session:
                request.session['name']=first
        return redirect('/success')
    return redirect ('/')


def success(request):
    if 'name' in request.session:
        return render(request,"success.html")
    return redirect ('/')

def logout(request):
    del request.session['name']
    return redirect('/')

def login(request):
    one_User=User.objects.filter(email=request.POST['lemail'])
    if one_User:
        if  bcrypt.checkpw(request.POST['lpassword'].encode(), one_User[0].pw_hash.encode()):
            if 'name' not in request.session:
                request.session['name']=one_User[0].first_name
            return redirect('/success')
        return redirect('/')
    return redirect('/')