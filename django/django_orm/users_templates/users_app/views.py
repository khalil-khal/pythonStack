from django.shortcuts import redirect, render
from .models import User


def index(request):
    context = {
        "allusers":User.objects.all()
    }
    return render(request,"index.html" ,context)

# Create your views here.
def new(request):
    if request.method =="POST":
        User.objects.create(first_name=request.POST['first'], last_name=request.POST['last'],email=request.POST['email'],age=request.POST['age'])
    return redirect("/")
