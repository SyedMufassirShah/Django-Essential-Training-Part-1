from django.db import models

# Create your models here.
class School(models.Model):
    # Id = models.AutoField(unique = True)
    Name = models.TextField(unique = True) 
    Email = models.EmailField(unique = True)
    Registered = models.BooleanField(default = False)