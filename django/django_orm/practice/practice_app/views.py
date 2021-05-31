from . import models
from django.shortcuts import redirect, render
from django.shortcuts import render,HttpResponse
def index(request):
    context={
        'books':models.allBooks()
    }
    return render(request,"index.html",context)

def addBook (request): #there is only request because there is no barameters in the route in urls
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        newly_created_Book=models.addOneBook(title,desc)
        #return render(request,'welcome.html')لما ينفذ الفنكشن لازم يبعتني عل هاي الصفحة
        return redirect('/')
    
def welcome(request,id):

    context={
        "this_book":models.getBook(id),
        'all Authers':models.allAuthers()
    }
    return render(request,"welcome.html",context)

def addAutherToBook(request,book_id):
    selected_auther_id=request.POST['selected_auther']
    selected_auther=models.Auther.objects.get(id=selected_auther_id)
    this_book=models.Book.objects.get(id=book_id)
    this_book=authers.add(selected_auther)
    return redirect("/shows/{book_id}")
