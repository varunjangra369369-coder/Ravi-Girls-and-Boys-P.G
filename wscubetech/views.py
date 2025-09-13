from django.shortcuts import render, redirect
from .models import Contact

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        return redirect('index')

    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        return redirect('index')
        
    return render(request, 'contact.html')

