from django.db import models

# Create your models here.
class TestModel1(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

class TestModel2(models.Model):
    header = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Test')