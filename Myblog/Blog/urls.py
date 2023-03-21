from django.contrib import admin
from django.urls import path
from django.urls import include
from Blog import views
urlpatterns = [
    path('', views.blogpage, name="blogpage"),
    path('blogpost/<slug:slug>', views.blogpost,name = "blogpost"),
    path('postcomment', views.postcomment,name = "postomment"),
    
]