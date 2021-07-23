from django.db import models

# Create your models here.
#create User model
from django.contrib.auth.models import AbstractUser
# Extend current user(Default by django) w/ Abstract user
# This model behaves identically to the default user model, but you’ll be able to customize it in the future if the need arises
# add your own profile fields and methods. AbstractBaseUser only contains the authentication functionality, but no actual fields
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email' # login w/ email, unique identifier.
    REQUIRED_FIELDS = [] 
    #has no effect in admin ui, it is list of the field names that will be prompted for when creating a user via the createsuperuser 

