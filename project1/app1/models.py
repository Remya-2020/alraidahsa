from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=15)  # Changed to CharField
    subject = models.CharField(max_length=200)  # Added subject field
    message = models.TextField()






