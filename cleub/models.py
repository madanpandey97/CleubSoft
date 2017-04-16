from django.contrib.auth.models import Permission, User
from django.db import models


class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=40)
    Message = models.TextField(max_length=500)
    

    def __str__(self):
        return self.Name 

class GetInTouch(models.Model):

    Email = models.EmailField(max_length=40)
    
    
    def __str__(self):
        return self.Email 
