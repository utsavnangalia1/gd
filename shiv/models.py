from pickle import FALSE, TRUE
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30,null=FALSE)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    desc =  models.TextField(max_length=222,null=FALSE)
    date = models.DateField()

    
    def __str__(self):
        return self.name

class Wallq(models.Model):
    serial = models.IntegerField(null=True)
    hashtag = models.CharField(max_length=20,null=True,default="Notdefined")
    question = models.CharField(max_length=2000,null=FALSE)
    answer = models.CharField(max_length=200)

    def  __str__(self):
            return self.question
        