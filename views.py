import contact
from django.shortcuts import render,redirect
from medilabbapp.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html' )

def start(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request, contact=None):
    if request.method == 'POST':
        contact = Contact(name=request.POST['name'],
                           email=request.POST['email'],
                           message=request.POST['message'],
                           phone=request.POST['phone'],
        return redirect('/contact')

    else:
        return render(request, 'contact.html')
