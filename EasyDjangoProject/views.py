from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm


# Create your views here.


def portada(request):
    return render(request, 'plantillasEasyDjango/portada.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('panel_de_control')
    else:
        form = AuthenticationForm()
    return render(request, 'plantillasEasyDjango/inicio_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('portada')

@login_required
def panel_de_control(request):
    return render(request, 'plantillasEasyDjango/panel_de_control.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('panel_de_control')  # Redirige a la página deseada
    else:
        form = RegistroForm()
    return render(request, 'plantillasEasyDjango/registro.html', {'form': form})



