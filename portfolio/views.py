from django.shortcuts import render,redirect
from portfolio.models import Contact
#below for mail sending
from django.conf import settings

# Create your views here.
def home(request):
    return render (request, 'home.html')
def about(request):
    return render (request, 'about.html')
def contact(request):
    if request.method == "POST":
        fname = request.POST.get('Name')
        femail = request.POST.get('email')
        fphone = request.POST.get('num')
        fdesc = request.POST.get('desc')
        query = Contact(name=fname,email=femail,phnumber=fphone,description=fdesc )
        query.save()


        #email sending from here
        


    return render (request, 'contact.html')
def resume(request):
    return render (request, 'resume.html')
def projects(request):
    return render (request, 'projects.html')
