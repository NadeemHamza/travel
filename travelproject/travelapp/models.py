from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    dsc = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Team(models.Model):
    mbr_name = models.CharField(max_length=100)
    mbr_img = models.ImageField(upload_to='pics')
    mbr_dsc = models.TextField(max_length=250)

    def __str__(self):
        return self.mbr_name
