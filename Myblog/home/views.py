from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
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