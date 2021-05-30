from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField

from login_app.models import *
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name='books', on_delete=CASCADE)
    users = models.ManyToManyField(User, related_name='favorite_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    