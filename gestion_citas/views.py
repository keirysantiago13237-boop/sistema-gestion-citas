from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Cita
from .forms import CitaForm


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_citas')
    else:
        form = UserCreationForm()
    return render(request, 'gestion_citas/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_citas')
    else:
        form = AuthenticationForm()
    return render(request, 'gestion_citas/login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


@login_required
def lista_citas(request):
    citas = Cita.objects.all().order_by('fecha')
    return render(request, 'gestion_citas/lista.html', {'citas': citas})


@login_required
def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'gestion_citas/formulario.html', {'form': form})


@login_required
def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'gestion_citas/formulario.html', {'form': form})


@login_required
def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    cita.delete()
    return redirect('lista_citas')
