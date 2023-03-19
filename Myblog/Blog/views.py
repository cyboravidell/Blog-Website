from django.shortcuts import render, HttpResponse

# Create your views here.

def blogpage(request):
    return render(request, 'Blog/blogpage.html')
    # return HttpResponse("This is a blog page. we will start soon so stay tuned !")

def blogpost(request):
    return render(request, 'Blog/blogpost.html')
    # return HttpResponse("This is blogpost : {slug}")