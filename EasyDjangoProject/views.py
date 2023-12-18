from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse

# Create your views here.

def portada(request):
    return render(request,'coffee-shop-html-template\index.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form,get_user())
            return redirect('panel_de_control')
    else:
        form = AuthenticationForm()
    return render(request, 'inicio_sesion.html', {'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('portada')

@login_required
def panel_de_control(request):
    return render(request, 'panel_de_control.html')

def paypal_integration(request):
    # Lógica de tu vista, si es necesario
    
    return render(request, 'paypal_integration.html')


