from django.db import models

# Create your models here.

class SignUpform(models.Model):
    username = models.CharField(max_length=150, unique=True)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=150)

    def __init__(self):
        return self.username
