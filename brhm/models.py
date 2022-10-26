from datetime import datetime
from tkinter import CASCADE
from django.db import models
from pickle import FALSE, TRUE
 

# Create your models here.

class Shabdkosh(models.Model):
    varna = models.CharField(max_length=10,null=False)
    meaning = models.TextField(max_length=100,blank=True,null=False)
    sanskt = models.CharField(max_length=20,null=False)
    eng = models.CharField(max_length=40,null=False)
    gramgp = models.CharField(max_length=50,null=False)
    varnhin = models.CharField(max_length=10,null=False)
    chak = models.CharField(max_length=10,null=False)

    def __str__(self):
        return self.sanskt

# # #whenever a varn is deleted from varnamala, corresponding varna from shabdkosh are deleted too

class Varnamala(models.Model):
    chakra = models.CharField(max_length=5,null=False)
    varn = models.CharField(max_length=5,null=False)
    angala = models.CharField(max_length=5,null=False)

    def _str_(self):
        return self.varn
    
class Blogpage(models.Model):
    hashtag = models.CharField(max_length=30,null=False)
    title = models.CharField(max_length=100,null=False)
    desc = models.TextField(max_length=1200,null=False)
    img = models.ImageField(null=False)
    link = models.TextField(max_length=20,null=False)
    read_time = models.CharField(max_length=20,null=False)
    author_name = models.CharField(max_length=40,null=False)
    date_uploaded = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.title
    

class Suktam(models.Model):
    suktam = models.TextField(max_length=500,null=False)
    sub_index = models.CharField(max_length=50,null=True)
    smskt = models.TextField(max_length=400,null=False)
    engsukt = models.TextField(max_length=600,null=False)
    engmean = models.TextField(max_length=600,null=False)

    def __str__(self):
        return self.suktam

class mantra(models.Model):
   mantra = models.CharField(max_length=50,null=False)
   smskt = models.TextField(max_length=300,null=False)
   engmantr = models.TextField(max_length=400,null=False)
   engmean = models.TextField(max_length=400,null=False)

   def __str__(self):
        return self.mantra

class strotam(models.Model):
    strota =  models.CharField(max_length=50,null=False)
    strtskt = models.CharField(max_length=500,null=False)
    strteng= models.TextField(max_length=500,null=False)
    strengmn = models.TextField(max_length=500,null=False)
    
    def __str__(self):
        return self.strota
    

class shlokas(models.Model):
    shloka =  models.CharField(max_length=50,null=False)
    shlokahead =  models.CharField(max_length=50,null=False)
    shlksnskt = models.CharField(max_length=500,null=False)
    shlkengconv= models.TextField(max_length=500,null=False)
    shlkengmean = models.TextField(max_length=500,null=False)
    
    def __str__(self):
        return self.shlokahead