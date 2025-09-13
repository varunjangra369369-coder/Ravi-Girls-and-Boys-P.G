from django.shortcuts import render 
from django.http import HttpResponse 

def about(request): 
    return render(request, 'about.html') 
def index(request): 
    context = {'greeting': 'Hello from Django'}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')