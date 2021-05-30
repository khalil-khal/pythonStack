from django import contrib
from django.contrib.messages.api import error
from django.db import models
from django.shortcuts import redirect, render
from django.contrib import messages
from . import models
# Create your views here.


def books(request):
    context = {
        'all_books': models.Book.objects.all()
    }
    return render(request, 'books.html', context)
    

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        errors = {}
        if len(description) < 5:
            errors['description'] = 'the description field must be at least 5 characters'
        if len(title) == 0:
            errors['title'] = 'the title field must be at least 1 characters'
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books')
        user = models.User.objects.get(id = request.session['id'])
        models.Book.objects.create(title = title, description = description, uploaded_by = user)
        return redirect('/render_books')
    redirect('/books')

def render_books(request):
    context = {
        'all_books': models.Book.objects.all()
    }
    return render(request, 'books.html', context)
            

def update_book(request, book_id):
    user = models.User.objects.get(id = request.session['id'])
    book = models.Book.objects.get(id = book_id)
    context = {
        'user':user,
        'book':book,
    }
    return render(request, 'update_book.html', context)

