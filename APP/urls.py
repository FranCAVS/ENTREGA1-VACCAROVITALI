from django.urls import path
from APP import views


urlpatterns = [
    path('lista-autos/', views.lista_autos),
    path('crear-autos/', views.crear_autos),
    path('lista-motos/', views.lista_motos),
    path('crear-motos/', views.crear_motos),
    path('licencias/', views.formulariolicencias, name="FormularioLicencias"),
    path('lista-licencias/', views.lista_registros, name="ListaLicencias"),
    path('buscar/', views.buscar, name="Buscar"),
]