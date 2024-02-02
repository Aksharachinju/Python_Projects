from django.db import models
# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='images')
    desc=models.TextField()
    def __str__(self):
        return self.name
class travelspots(models.Model):
    tname=models.CharField(max_length=250)
    timg=models.ImageField(upload_to='images')
    det=models.TextField()
    def __str__(self):
        return self.tname

