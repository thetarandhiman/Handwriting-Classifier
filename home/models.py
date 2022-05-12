
# Create your models here.

from django.db import models
  
class img(models.Model):
    name = models.CharField(max_length=50)
    Training_Img = models.ImageField(upload_to='images/')