from django.db import models
from django.db.models.base import Model

# Create your models here.

class Category(models.Model):
    cat_name=models.CharField(max_length=100,blank=False )
    

    def __str__(self):
        return self.cat_name

class Location(models.Model):
    loc_name=models.CharField(max_length=50,blank=False )
    

    def __str__(self):
        return self.loc_name



class Image(models.Model):
    Image=models.ImageField(null=True,blank=False)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=4000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.description





