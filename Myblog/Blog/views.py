from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib import messages
# Create your views here.

def blogpage(request):
    allposts = Post.objects.all()

    context = {'allposts' : allposts}
    print(allposts)
    return render(request, 'Blog/blogpage.html', context)
    # return HttpResponse("This is a blog page. we will start soon so stay tuned !")

def blogpost(request, slug):

    post  = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {"post" : post, "comments": comments, "user": request.user}
    return render(request, 'Blog/blogpost.html', context)
    # return HttpResponse("This is blogpost : {slug}")

def postcomment(request):
   
    if request.method == "POST":
        comment = request.POST.get('postcomment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(Sno = postSno)
        comment = BlogComment(comment=comment, user = user, post = post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    return redirect(f"/blog/blogpost/{post.slug}")