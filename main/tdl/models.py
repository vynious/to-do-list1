from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
from user.models import User
# Create your models here.

# User= settings.AUTH_USER_MODEL

class ToDoList(models.Model): 
    
    levels= [
        ('H','HIGH'),
        ('M','MID'),
        ('L','LOW'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created= models.DateTimeField(default=now,editable=False)
    content = models.CharField(blank=False, max_length=120)
    priority = models.CharField(choices=levels, max_length=2)

