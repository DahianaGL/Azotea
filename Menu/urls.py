from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('menu', views.menu, name="Menu"),
    path('plato/<int:id>', views.detalle_plato, name='DetallePlato'),
]
