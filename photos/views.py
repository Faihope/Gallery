from django.shortcuts import render
from .models import Category,Image

# Create your views here.
def gallery(request):
    categories= Category.objects.all()
    context= {'categories':categories}
    return render(request,'gallery.html',context)

def viewPhoto(request,pk=int):
    return render(request,'photo.html')

def addPhoto(request):
    return render(request,'add.html')

