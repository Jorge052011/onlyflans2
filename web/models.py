from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField("Producto", max_length=50)
    descripcion = models.TextField("Descripcion")
    precio = models.DecimalField("Precio", max_digits=5, decimal_places=0)
    stock = models.PositiveIntegerField("Stock", default=0)
    imagen = models.ImageField("Imagen",upload_to="productos/")
    premium = models.BooleanField("Premium", default=False)

    def __str__(self):
        return self.nombre_producto



class ContactForm(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"