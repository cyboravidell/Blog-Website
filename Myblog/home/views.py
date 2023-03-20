from django.shortcuts import render,redirect, HttpResponse
from home.models import Contact
from Blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request,"home/home.html")
    # return HttpResponse("This the Home Page")

def about(request):
    return render(request,"home/about.html")
    # return HttpResponse("This the About Page")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 3 or len(email)<5 or  len(phone)<10 or  len(content) < 10:
            messages.error(request, "Please fill the form properly")
        else:
            contact = Contact(name = name, email = email, phone = phone, content = content )
            contact.save()
            messages.success(request, "Your response has been submitted succesfully")
        
    # print(name,email,phone,content)
    return render(request,"home/contact.html")
    # return HttpResponse("This the Contact Page")

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allposts = Post.objects.none()
    else:
        if Post.objects.filter(title__icontains=query):
            allposts = Post.objects.filter(title__icontains=query)
        elif Post.objects.filter(author__icontains=query):
            allposts = Post.objects.filter(author__icontains=query)
        else:
            allposts = Post.objects.filter(content__icontains=query)
    
    if allposts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query")
    params = {'allposts' : allposts,
              'query': query}
    return render(request, 'home/search.html', params)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['inputfname']
        lname = request.POST['inputlname']
        email = request.POST['inputemail']
        pass1 = request.POST['inputPassword1']
        pass2 = request.POST['inputPassword2']

        # check for errorneous input
        if len(username)>10:

            if username.isdigit():
                messages.error(request, "Your username must contain atleast 1 character")

            messages.error(request, "Your username must be less than 10 characters")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request,"Password do not match, Please check the password and try again")
            return redirect('home')
        
        # Creating User
        else:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request,"Your account has been created Successfully")
        return redirect('home')
    
def blogsignin(request):
    if request.method == "POST":

        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)
        if user is None:
            messages.error(request, "Invalid Credentials, Please check and retry again")
            return redirect('home')
        else:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
    else:
        HttpResponse("404 - Not Found")


def bloglogout(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('home')