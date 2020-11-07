from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'home.html',{})

def gallery(request):
    return render(request,'gallery.html',{})

def about(request):
    return render(request,'about.html',{})
