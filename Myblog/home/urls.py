from django.contrib import admin
from django.urls import path
from django.urls import include
from home import views
urlpatterns = [
    path('', views.home, name= "home"),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name = "contact"),
    path('search', views.search, name="search"),
    path('signup', views.signup, name="signup"),
    path('signin', views.blogsignin, name="blogsignin"),
    path('logout', views.bloglogout, name="bloglogout"),
]