from django.http.request import HttpRequest
from django.shortcuts import render,redirect
from . import models
import re
from django.contrib import messages
import bcrypt
from .models import *
from . import models


def index(request):
    return render(request,"index.html")

def registration(request):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors={}
    if len(request.POST['fname'])<2:
        errors['fname']='first name is too short' #بنادي على الفيرست نيم عن طريق النيم الي بال اتش تي ام ال
    if len(request.POST['lname'])<2:
        errors['lname']='last name is too short'

    if not EMAIL_REGEX.match(request.POST['email']):
        errors['email']="invalid email address"
    if len(request.POST['password'])<8:
        errors['password']='short password'
    if request.POST["password"] != request.POST["confirm"]:
        errors['confirm']='Not matching'

    if messages:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    first_name=request.POST["fname"]
    last_name=request.POST["lname"]
    email=request.POST["email"]
    password=request.POST["password"]
    confirm_password=request.POST["confirm"]
    print(request.POST)
    if password == confirm_password :
        print("both passwords are equals")
        hash =  bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        models.User.objects.create(first_name=first_name,last_name=last_name,email=email,password=hash)
        print("values added to the database")
        if 'name' not in request.session:
            request.session['name']=first_name
            request.session['last_name'] = last_name
            print("session variables created successfully")
            return redirect('/success')
    return redirect ('/')

#  request.session['id'] = 5
def success(request):
    if 'name' in request.session:
        return render(request,"success.html")
    return redirect ('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    one_User=User.objects.filter(email=request.POST['email'])
    if one_User[0]:
        if  bcrypt.checkpw(request.POST['password'].encode(), one_User[0].password.encode()):
            if 'name' not in request.session:
                request.session['name']=one_User[0].first_name
                request.session['last_name'] = one_User[0].last_name
            return redirect('/success')
    return redirect('/')