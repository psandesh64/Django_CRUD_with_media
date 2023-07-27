from django.db import models

# Create your models here.
class Students(models.Model):
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    b_group = models.CharField(max_length=3,
                               choices=(('A','A+'),('B','B+'),('O','O+'))
                               )