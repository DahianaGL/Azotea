from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('servicios/', views.servicios, name="Servicios"),
]
#Enrutamientos para la carpeta media
