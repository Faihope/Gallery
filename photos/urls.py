from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns=[
   url('^$',views.gallery,name='gallery'),
    path('photo/<str:pk>',views.viewPhoto,name='photo'),
    url('add',views.addPhoto,name='add')
]

