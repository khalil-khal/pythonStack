from django.db import models

class dojos (models.Model):
    name=models.CharField(max_length=225)
    City=models.CharField(max_length=255)
    state= models.CharField(max_length=2)

class ninjas(models.Model):
    title= models.CharField(max_length=255)
    dojos=models.ForeignKey(dojos,related_name='ninjas',on_delete = models.CASCADE)
    first_name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


