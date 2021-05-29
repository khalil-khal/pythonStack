from typing import ContextManager
from django.shortcuts import redirect, render
from . import models

# Create your views here.
def shows(request):
    Context={
        'all_shows':models.all_shows()
    }
    return render(request,'shows.html',Context)


def new(request):
    return render(request,'new_show.html')

def add_shows(request):
    if request.method == "POST":
        title=request.POST['title']
        network=request.POST['network']
        released_date=request.POST['rd']
        des=request.POST['des']
        id = models.add_shows(title,network,released_date,des)
        return redirect('/shows/'+str(id))
    return redirect('/')
        

def view_show (request,id):
    show = models.get_id(id)
    context={
        'show':show
    }
    return render(request,"view_show.html",context)


def show_edit(request,id):
    show = models.get_id(id)
    context={
        'show':show
    }
    return render(request,"edit_show.html",context)
    

def edit_show(request):
    return render(request,'edit_show.html')