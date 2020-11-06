from django.shortcuts import render

# Create your views here.
def main(response):
    return render(response,'home.html',{})

def galeria(response):
    return render(response,'galeria.html',{})