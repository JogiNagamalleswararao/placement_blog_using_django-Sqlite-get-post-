from django.db import models
from datetime import datetime
# Create your models here.
"""class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    describe=models.CharField(max_length=100)
    create_at=models.DateTimeField(default=datetime.now)
    def __str__(self) -> str:
        return self.title"""
class Job(models.Model):
    image=models.CharField(max_length=10000)
    Com=models.CharField(max_length=100)
    Rol=models.CharField(max_length=100)
    Edu=models.CharField(max_length=100)
    Sal=models.CharField(max_length=100)
    Exp=models.CharField(max_length=100)
    Las=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
    describe=models.CharField(max_length=10000)
    create_at=models.CharField(max_length=10000)
    def __str__(self) -> str:
        return self.Com
class feedback(models.Model):
    name=models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    #if dont mention null it showing some error
    area=models.CharField(max_length=10000,null=True)
    def __str__(self) -> str:
        return self.name


