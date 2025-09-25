from django.contrib import admin
from .models import Producto
from .models import ContactForm

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass



@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    pass
