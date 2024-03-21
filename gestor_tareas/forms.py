from django.forms import ModelForm
from .models import Tarea

class Formulario_Tarea(ModelForm):
  class Meta:
    model = Tarea
    fields = ['titulo', 'descripcion', 'importancia']