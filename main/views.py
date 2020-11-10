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
        elif n_habitaciones == '4' and n_baños == '1':
            ctx['casa'] = '4-1'
        elif n_habitaciones == '3' and n_baños == '2':
            ctx['casa'] = '3-2'
        elif n_habitaciones == '3' and n_baños == '1':
            ctx['casa'] = '3-1'
        elif n_habitaciones == '2' and n_baños == '2':
            ctx['casa'] = '2-2'
        elif n_habitaciones == '2' and n_baños == '1':
            ctx['casa'] = '2-1'
        elif n_habitaciones == '1' and n_baños == '2':
            ctx['casa'] = '1-2'
        elif n_habitaciones == '1' and n_baños == '1':
            ctx['casa'] = '1-1'
    return render(request,'medida.html',ctx)

def metraje(request):
    ctx = {}
    ctx['metros'] = ''
    if request.method == 'GET':
        metros_cuadrados = str(request.GET.get('metros_cuadrados'))
        if metros_cuadrados != 'None':
            lbl_precio = round((float(metros_cuadrados)*33000)/28883.18,2)
        else:
            metros_cuadrados = '0'
            lbl_precio = '0'
   
    return render(request,'metraje.html', {'metros_cuadrados': metros_cuadrados,'lbl_precio': lbl_precio })
