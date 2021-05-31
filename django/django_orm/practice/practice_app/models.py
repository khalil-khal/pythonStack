from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Auther(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    books = models.ManyToManyField(Book, related_name="author")
    notes = models.TextField(default='Author notes' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

def addOneBook(title,desc):
    new_Book=Book.objects.create(title=title,desc=desc)
    return new_Book

def allBooks():
    return Book.objects.all()

def getBook(id):
    return Book.objects.get(id=id)

def allAuthers():
    return Auther