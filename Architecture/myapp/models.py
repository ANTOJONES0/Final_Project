from django.db import models

class Datas(models.Model):
    Message = models.CharField(max_length=400,default='')
    Company = models.CharField(max_length=100,default='')
    Place = models.CharField(max_length=40,default='')
    Email = models.CharField(max_length=20,default='')
    Phone = models.IntegerField(default='')


