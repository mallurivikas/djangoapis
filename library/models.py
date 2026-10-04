from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100, db_index=True)
    author=models.CharField(max_length=100)
    price=models.FloatField()
    
