from django.db import models
from django.contrib.auth.models import AbstractUser , AbstractBaseUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True,blank=True)

    