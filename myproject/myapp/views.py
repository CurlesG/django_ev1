from django.shortcuts import render

# Create your views here.


def home(request):
    return render (request, 'home.html')

def services(request):
    return render (request, 'services.html')

def checklist(request):
    return render (request, 'checklist.html')

def contact(request):
    return render (request, 'contact.html')

def data(request):
    return render (request, 'data.html')

def dashboard(request):
    return render (request, 'dashboard.html')

def test(request):
    return render (request, 'test.html')