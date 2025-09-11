from django.urls import path, include
from mi_app.views import *
from mi_app.views.views_administrador import *
from mi_app.views.views_cliente import *
from mi_app.views.views_proveedor import *
from mi_app.views.views_marca import *
app_name = 'mi_app'
urlpatterns = [
   #path('index.html', vista, name='index'),
    
   #_________________________ Modulo de Administrador __________________________
    path('administradores/listar/', AdministradorListView.as_view(), name='administrador_lista'),
    path('administradores/crear/', AdministradorCreateView.as_view(), name='administrador_crear'),
    path('administradores/editar/<int:pk>/', AdministradorUpdateView.as_view(), name='administrador_editar'),
    path('administradores/eliminar/<int:pk>/', AdministradorDeleteView.as_view(), name='administrador_eliminar'),

    
#_________________________modulo clientes_________________________________________
    path('clientes/listar/', clienteListView.as_view(), name='cliente_lista'),
    path('clientes/crear/', clienteCreateView.as_view(), name='cliente_crear'),
    path('clientes/editar/<int:pk>/', clienteupdateView.as_view(), name='cliente_editar'),
    path('clientes/eliminar/<int:pk>/', clienteDeleteView.as_view(), name='cliente_eliminar'),

    
#_________________________modulo proveedores_________________________________________
    path('proveedores/listar/', proveedorListView.as_view(), name='proveedor_lista'),
    path('proveedores/crear/', proveedorCreateView.as_view(), name='proveedor_crear'),
    path('proveedores/editar/<int:pk>/', proveedorupdateView.as_view(), name='proveedor_editar'),
    path('proveedores/eliminar/<int:pk>/', proveedorDeleteView.as_view(), name='proveedor_eliminar'),  
    
    
#_________________________modulo marcas_________________________________________
    path('marcas/listar/', marcaListView.as_view(), name='marca_lista'),    
    path('marcas/crear/', marcaCreateView.as_view(), name='marca_crear'),
    path('marcas/editar/<int:pk>/', marcaupdateView.as_view(), name='marca_editar'),
    path('marcas/eliminar/<int:pk>/', marcaDeleteView.as_view(), name='marca_eliminar'),    
]
# 