from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0,null=True,blank=True)
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    email = models.EmailField(max_length=254,unique=True,null=True,blank=True)
