from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class User(AbstractUser):
    tweet_id = models.CharField(max_length=100, blank=True)
    drive_link = models.CharField(max_length=500, blank=True)