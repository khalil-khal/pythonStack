from django.db import models

# Create your models here.
class shows(models.Model):
    Title= models.CharField(max_length=255)
    Network= models.CharField(max_length=255)
    Release_Date=models.DateField()
    Des=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def all_shows():
    all_shows=shows.objects.all()
    return all_shows

def add_shows(title,network,rd,des):
    x=shows.objects.create(Title=title,Network=network,Release_Date=rd,Des=des)
    return x.id

def get_id(id):
    show  = shows.objects.get(id=id)
    return show