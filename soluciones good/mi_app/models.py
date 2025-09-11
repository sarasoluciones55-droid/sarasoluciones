from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Administrador(models.Model):
 
    nombres_completos = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    contraseña = models.CharField(max_length=128, default="")
    cedula = models.CharField(max_length=20, default="")
    telefono = models.CharField(max_length=15, default="")

    
    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        
    def __str__(self):
        return f"{self.nombres_completos} {self.cedula}"
        
 


class Proveedor(models.Model):
    """Modelo para proveedores"""
    nombre_completo = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=50, blank=True, null=True)
    numero_documento_nit = models.CharField(max_length=15, unique=True)
    direccion_empresa = models.CharField(max_length=30)
    numero_telefonico = models.CharField(max_length=15)
    descripcion = models.TextField(max_length=100)
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        
    def __str__(self):
        return self.nombre_completo


class GestionCliente(models.Model):
    """Modelo para gestión de clientes"""
    nombre_completo = models.CharField(max_length=100)
    numero_telefonico = models.CharField(max_length=50,null=True,blank=True)
    numero_documento = models.CharField(max_length=50, unique=True)
    correo_electronico = models.EmailField(max_length=50)
    contrasena = models.CharField(max_length=50)  # En producción usar User de Django
    
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
    def __str__(self):
        return self.nombre_completo


class Marca(models.Model):
    """Modelo para marcas de productos"""
    nombre_marca = models.CharField(max_length=80, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    logo_marca = models.ImageField(upload_to='logos/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        
    def __str__(self):
        return self.nombre_marca


class PresentacionTipo(models.Model):
    """Modelo para tipos de presentación de productos"""
    nombre = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    funcion_principal = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=60)
    
    class Meta:
        verbose_name = "Tipo de Presentación"
        verbose_name_plural = "Tipos de Presentación"
        
    def __str__(self):
        return f"{self.nombre} - {self.modelo}"


class Categoria(models.Model):
    """Modelo para categorías de productos"""
    nombre_categoria = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(max_length=100)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        
    def __str__(self):
        return self.nombre_categoria


class Producto(models.Model):
    """Modelo principal para productos"""
    # Relaciones con otras tablas
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos')
    id_presentacion = models.ForeignKey(PresentacionTipo, on_delete=models.CASCADE, related_name='productos')
    
    # Campos del producto
    nombre_producto = models.CharField(max_length=100)
    cantidad_producto = models.IntegerField(validators=[MinValueValidator(0)])
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    estado_producto = models.CharField(max_length=30)
    
    # Timestamps
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        
    def __str__(self):
        return f"{self.nombre_producto} - {self.id_marca.nombre_marca}"


class GestionServicio(models.Model):
    """Modelo para gestión de servicios"""
    nombre_servicio = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    valor = models.CharField(max_length=50)  # Podría ser DecimalField si es monetario
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        
    def __str__(self):
        return self.nombre_servicio


class GestionGarantia(models.Model):
    """Modelo para gestión de garantías"""
    id_factura = models.IntegerField()  # Referencia a factura
    descripcion_garantia = models.TextField(max_length=255)
    fecha_garantia = models.DateField()
    estado_garantia = models.CharField(max_length=20, default='ACTIVA')
    
    class Meta:
        verbose_name = "Garantía"
        verbose_name_plural = "Garantías"
        
    def __str__(self):
        return f"Garantía - Factura #{self.id_factura}"


class Facturacion(models.Model):
    """Modelo para facturación"""
    # Relaciones
    id_admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    id_venta = models.IntegerField()  # Referencia a venta
    id_servicio = models.ForeignKey(GestionServicio, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Campos de factura
    fecha_facturacion = models.DateField()
    descripcion_venta = models.TextField(max_length=255)
    terminos_condiciones = models.TextField(max_length=255)
    nit = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        
    def __str__(self):
        return f"Factura #{self.id} - {self.fecha_facturacion}"


class Compra(models.Model):
    """Modelo para compras a proveedores"""
    id_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    numero_documento_nit_proveedor = models.CharField(max_length=15)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_productos = models.IntegerField(validators=[MinValueValidator(1)])
    observaciones = models.TextField(max_length=60, blank=True)
    fecha_compra = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        
    def __str__(self):
        return f"Compra #{self.id} - {self.fecha_compra}"


class GestionPedido(models.Model):
    """Modelo para gestión de pedidos de clientes"""
    id_cliente = models.ForeignKey(GestionCliente, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre_de_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    departamento_entrega = models.CharField(max_length=50)
    municipio_ciudad_entrega = models.CharField(max_length=50)
    direccion_entrega = models.CharField(max_length=50)
    comprobante_pago = models.CharField(max_length=50)  # Podría ser FileField
    estado_pedido = models.CharField(max_length=20, default='PENDIENTE')
    numero_gestion_de_venta = models.IntegerField()
    email = models.EmailField(max_length=50)
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        
    def __str__(self):
        return f"Pedido #{self.id} - {self.id_cliente.nombre_completo}"


class Ventas(models.Model):
    """Modelo para registro de ventas"""
    id_pedido = models.ForeignKey(GestionPedido, on_delete=models.CASCADE)
    comprobante_pago = models.CharField(max_length=50)
    fecha_venta = models.DateField()
    id_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        
    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta}"