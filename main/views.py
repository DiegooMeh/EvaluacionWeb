from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'home.html',{})

def gallery(request):
    return render(request,'gallery.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def medida(request):
    return render(request,'medida.html',{})

def metraje(request):
    return render(request,'metraje.html',{})
