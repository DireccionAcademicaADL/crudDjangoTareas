from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import Formulario_Tarea
from .models import Tarea


# Create your views here.

def home(request):
  def get(self, request):
        return render(request, 'home.html')


#def sign_up(request):
  return render(request, 'signup.html', )
def sign_up(request):
  if request.method == 'GET':
    return render(request, 'signup.html', {'form': UserCreationForm})
  else:
    #Registrando el usuario
    if request.POST['password1']==request.POST['password2']:
      try:
        user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
        user.save()
        login(request, user)
        return redirect('tareas')  
      except:
        return HttpResponse("Elusuario ya existe")
    return HttpResponse("Las contraseñas no coinciden")
  

def sign_out(request):
  logout(request)
  return redirect('home')


def log_in(request):
  if request.method=="GET":
    return render(request, 'login.html', {
      'form': AuthenticationForm
    })
  else:
    user = authenticate(request, 
                        username=request.POST['username'], 
                        password=request.POST["password"])
    if user is None:
      return render(request, 'login.html', {
        'form': AuthenticationForm, 
        'error': 'El usuario o contraseña son incorrectos'
      })
    else:
      login(request, user)
      return redirect('tareas')

@login_required
def tareas(request):
  tareas = Tarea.objects.filter(user=request.user)
  return render(request, 'tareas.html', {'tareas': tareas})

def crear_tarea(request):
  if request.method == 'GET':
    return render(request, 'crear_tarea.html', {'form': Formulario_Tarea})
  else:
    try:
      form = Formulario_Tarea(request.POST)
      nueva_tarea = form.save(commit=False)
      nueva_tarea.user = request.user
      nueva_tarea.save()
      return redirect('tareas')
    except ValueError:
      return render(request, 'crear_tarea.html', {'form': Formulario_Tarea, 'error': 'Ingresa datos válidos en la tarea'})

def detalle_tarea(request, tarea_id):
  if request.method == 'GET':
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    form = Formulario_Tarea(instance=tarea)
    return render(request, 'detalle_tarea.html', {'tarea': tarea, 'form': form})
  else:
    try:
      tarea = get_object_or_404(Tarea, pk=tarea_id)
      form = Formulario_Tarea(request.POST, instance=tarea)
      form.save() 
      return redirect('tareas')
    except:
      return render(request, 'detalle_tarea.html', {
        'tarea': tarea, 
        'form': form, 
        'error': 'Se ha generado un error actualizando la tarea'
        })

def borrar_tarea(request, tarea_id):
  tarea = get_object_or_404(Tarea, pk=tarea_id)
  tarea.delete()
  return redirect('tareas')