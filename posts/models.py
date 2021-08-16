from django.db import models

# Create your models here.
class User(models.Model):
    """Clase Model"""
    email = models.EmailField()
    password = models.CharField()

    first_name = models.CharField()
    last_name = models.CharField()

    bio = models.TextField()

    birthdate = models.DateField()

    