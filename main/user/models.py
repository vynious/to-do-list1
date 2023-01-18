from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.




class UserManager(auth_models.BaseUserManager):
    def create_user(self,email:str,first_name:str,last_name:str,password:str=None,is_staff=True,is_superuser=False):
        if not email:
            raise ValueError('User must have an email')
        if not first_name:
            raise ValueError('User must have a first name')
        if not last_name:
            raise ValueError('User must have a last name')

        user= self.model(
            email=self.normalize_email(email),
            # first_name=first_name,
            # last_name=last_name,
        )
        user.first_name=first_name
        user.last_name=last_name
        user.set_password(password)
        user.is_active=True
        user.is_staff=is_staff
        user.is_superuser=is_superuser
        user.save()
        return user

    def create_superuser(self,first_name,last_name,email,password):
        user= self.create_user( # calls the base function create_user and replaces the value to make it a superuser by replacing True/False
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()
        return user

class User(auth_models.AbstractUser):
    # first_name and last_name already included in the AbstractUser model. 
    first_name = models.CharField(verbose_name='First Name', max_length=255)
    name_name = models.CharField(verbose_name='Last Name', max_length=255)
    email = models.EmailField(verbose_name='Email', unique=True, max_length=255)
    password = models.CharField(verbose_name='Password',max_length=255)
    username = None # get rid of the already included username field in AbstractUser model

    objects=UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

