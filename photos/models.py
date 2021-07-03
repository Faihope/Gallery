from django.db import models
from django.db.models.base import Model

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100,blank=True,null=True )
    

    def __str__(self):
        return self.category_name

    @classmethod
    def search_by_category_name(cls,search_term):
        category = cls.objects.filter(category_name__icontains=search_term)
        return category

class Location(models.Model):
    location_name=models.CharField(max_length=50,blank=False ,null=True)
    

    def __str__(self):
        return self.location_name



class Image(models.Model):
    image=models.ImageField(null=True,blank=False)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=4000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def save_image(self):
        self.save()





