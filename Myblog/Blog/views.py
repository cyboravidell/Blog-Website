from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.

def blogpage(request):
    allposts = Post.objects.all()

    context = {'allposts' : allposts}
    print(allposts)
    return render(request, 'Blog/blogpage.html', context)
    # return HttpResponse("This is a blog page. we will start soon so stay tuned !")

def blogpost(request, slug):
    print(slug)
    post  = Post.objects.filter(slug=slug).first()
    context = {"post" : post}
    return render(request, 'Blog/blogpost.html', context)
    # return HttpResponse("This is blogpost : {slug}")