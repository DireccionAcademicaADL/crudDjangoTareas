from django.contrib import admin
from django.urls import path
from gestor_tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('signup/', views.sign_up, name="signup"),
    path('tareas/', views.tareas, name="tareas"),
    path('logout/', views.sign_out, name="logout"),
    path('login/', views.log_in, name="login"),
    path('crearTarea/', views.crear_tarea, name="crearTarea"),
    path('detalleTarea/<int:tarea_id>', views.detalle_tarea, name="detalleTarea"),
    path('detalleTarea/<int:tarea_id>/delete', views.borrar_tarea, name="borrarTarea"),
]
