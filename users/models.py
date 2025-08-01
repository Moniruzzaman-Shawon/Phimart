from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
# Create your models here.

class User(AbstractUser): # abstract user has username, email by default 
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15,blank=True, null=True)

    USERNAME_FIELD = 'email' # use email instead of username
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email