from django.urls import path, include
from mi_app.views import *
from mi_app.views.views_administrador import *
from mi_app.views.views_cliente import *
from mi_app.views.views_proveedor import *
from mi_app.views.views_marca import *
from mi_app.views.views_presentacionTipo import *
from mi_app.views.views_cateroria import *
from mi_app.views.views_producto import *
from mi_app.views.views_gestionservicio import *
from mi_app.views.views_garantia import *
from mi_app.views.views_pedido import *
from mi_app.views.views_factura import *
from mi_app.views.views_ventas import *


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
    
    
#_________________________modulo presentacionTipo_________________________________________
    path('presentacionTipo/listar/', presentacionTipoListView.as_view(), name='presentacionTipo_lista'),    
    path('presentacionTipo/crear/', presentacionTipoCreateView.as_view(), name='presentacionTipo_crear'),
    path('presentacionTipo/editar/<int:pk>/', presentacionTipoupdateView.as_view(), name='presentacionTipo_editar'),
    path('presentacionTipo/eliminar/<int:pk>/', presentacionTipoDeleteView.as_view(), name='presentacionTipo_eliminar'),   
    
#_________________________modulo categoria_________________________________________
    path('categoria/listar/', categoriaListView.as_view(), name='categoria_lista'), 
    path('categoria/crear/', categoriaCreateView.as_view(), name='categoria_crear'),
    path('categoria/editar/<int:pk>/', categoriaupdateView.as_view(), name='categoria_editar'),
    path('categoria/eliminar/<int:pk>/', categoriaDeleteView.as_view(), name='categoria_eliminar'),
    
#--------------------------------modulo producto ---------------------------------------

       path('producto/listar/', productoListView.as_view(), name='producto_lista'),
       path('producto/crear/', productoCreateView.as_view(), name='producto_crear'),
       path('producto/editar/<int:pk>/', productoupdateView.as_view(), name='producto_editar'),
       path('producto/eliminar/<int:pk>/', productoDeleteView.as_view(), name='producto_eliminar'),
           
#--------------------------------modulo gestion servicio ---------------------------------------
       path('gestionservicio/listar/', servicioListView.as_view(), name='gestionservicio_lista'),
       path('gestionservicio/crear/', servicioCreateView.as_view(), name='gestionservicio_crear'),
       path('gestionservicio/editar/<int:pk>/', serviciopdateView.as_view(), name='gestionservicio_editar'),
       path('gestionservicio/eliminar/<int:pk>/', servicioDeleteView.as_view(), name='gestionservicio_eliminar'),  
 
 
 #--------------------------------modulo garantia ---------------------------------------
       path('garantia/listar/', garantiaListView.as_view(), name='garantia_lista'),
       path('garantia/crear/', garantiaCreateView.as_view(), name='garantia_crear'),
       path('garantia/editar/<int:pk>/', garantiaupdateView.as_view(), name='garantia_editar'),
       path('garantia/eliminar/<int:pk>/', garantiaDeleteView.as_view(), name='garantia_eliminar'),  
     
#--------------------------------modulo pedido ---------------------------------------
        path('pedido/listar/', pedidoListView.as_view(), name='pedido_lista'),   
        path('pedido/crear/', pedidoCreateView.as_view(), name='pedido_crear'),
        path('pedido/editar/<int:pk>/', pedidoUpdateView.as_view(), name='pedido_editar'),
        path('pedido/eliminar/<int:pk>/', pedidoDeleteView.as_view(), name='pedido_eliminar'),
      
      
#--------------------------------modulo facturacion ---------------------------------------
        path('factura/listar/', FacturaListView.as_view(), name='factura_lista'),   
        path('factura/crear/', FacturaCreateView.as_view(), name='factura_crear'),
        path('factura/editar/<int:pk>/', FacturaUpdateView.as_view(), name='factura_editar'),
        path('factura/eliminar/<int:pk>/', facturaDeleteView.as_view(), name='factura_eliminar'),      
            

#--------------------------------modulo ventas ---------------------------------------
        path('ventas/listar/', ventasListView.as_view(), name='ventas_lista'),
        path('ventas/crear/', ventasCreateView.as_view(), name='ventas_crear'),
        path('ventas/editar/<int:pk>/', ventasUpdateView.as_view(), name='ventas_editar'),
        path('ventas/eliminar/<int:pk>/', ventasDeleteView.as_view(), name='ventas_eliminar'),
                  
]

