from django.contrib import admin
from django.urls import path
from django.urls import include
from Blog import views
urlpatterns = [
    path('', views.blogpage, name="blogpage"),
    path('blogpost', views.blogpost,name = "blogpost"),
    
]