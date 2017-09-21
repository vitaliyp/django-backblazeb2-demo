from django.db import models

class JustFile(models.Model):
    myfile = models.FileField(upload_to='files') 
    size = models.IntegerField()
