from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    description = models.TextField()

def __str__(self):
    return self.name

class Student(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)

def __str___(self):
    return self.name

class Model(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField()

def __str___(self):
    return self.name

class Cars(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField()