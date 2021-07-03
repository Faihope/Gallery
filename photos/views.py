from django.shortcuts import render
from .models import Category,Image,Location

# Create your views here.
def gallery(request):
    categories= Category.objects.all()
    photos=Image.objects.all()
    context= {'categories':categories, 'photos':photos}
    
    return render(request,'gallery.html',context)

def viewPhoto(request,pk=int):
    photo=Image.objects.get(id=pk)
    return render(request,'photo.html',{'photo':photo})

def addPhoto(request):
    categories= Category.objects.all()

    context= {'categories':categories}
    return render(request,'add.html',context)
    

