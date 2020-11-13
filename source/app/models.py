from django.db import models

# Create your models here.

class Testdb(models.Model):
    name = models.CharField(max_length=20)

class User1(models.Model):
    name = models.CharField(max_length=20)