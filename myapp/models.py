from email.policy import default
from django.db import models
from django.urls import path

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
class Image(models.Model):
    title=models.CharField(max_length=2000000)
    description= models.TextField()

    image=models.FileField(upload_to='images')
    amount=models.CharField(max_length=10, default=0)
    added_date=models.DateTimeField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)







    def __str__(self):
        return self.title