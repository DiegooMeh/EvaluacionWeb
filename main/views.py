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
    ctx = {}
    ctx['casa'] = ''
    if request.method == 'GET':
        n_habitaciones = request.GET.get('n_habitaciones')
        n_baños = request.GET.get('n_baños')
        if n_habitaciones == '4' and n_baños == '2':
            ctx['casa'] = '4-2'
        
    return render(request,'medida.html',ctx)

def metraje(request):
    return render(request,'metraje.html',{})
