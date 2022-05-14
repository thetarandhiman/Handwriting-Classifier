
# Create your models here.

from django.db import models
  
def custom(instance, filename):
    filename="User1.png"
    return filename

def custom2(instance, filename):
    filename="User2.png"
    return filename

def custom3(instance, filename):
    filename="test.png"
    return filename

class img(models.Model):
    name = models.CharField(max_length=50)
    Training_Img = models.ImageField(upload_to=custom)

class img2(models.Model):
    name = models.CharField(max_length=50)
    Training_Img = models.ImageField(upload_to=custom2)

class img3(models.Model):
    Testing_Img = models.ImageField(upload_to=custom3)