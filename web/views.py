from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Producto
from django.views.generic import DetailView
from .forms import ContactFormForm
from django.contrib import messages
from django.urls import reverse
from .forms import ContactFormModelForm

# Create your views here.

def home(request):
    flanes = Producto.objects.all().filter(premium="False")
    return render(request, "web/home.html", {"flanes":flanes})

@login_required
def home_premium(request):
    flanes = Producto.objects.all().filter(premium="True")

    return render(request, "web/home_premium.html", {"flanes":flanes})


class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'web/detalle_producto.html'
    context_object_name = 'flan'

def acerca(request):
    return render(request, "web/acerca.html")

def bienvenido_cliente(request):
    return render(request, "web/bienvenido.html")

def contacto_view(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # Aquí podrías guardar en BD si quieres
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            
            # Mensaje de éxito
            messages.success(request, "Gracias por contactarte con OnlyFlans, te responderemos en breve")
            return redirect(reverse("contacto_exito"))
    else:
        form = ContactFormForm()

    return render(request, "web/contacto.html", {"form": form})

def contacto_exito_view(request):
    return render(request, "web/contacto_exito.html")


def contacto_view(request):
    if request.method == "POST":
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Gracias por contactarte con OnlyFlans, te responderemos en breve")
            return redirect(reverse("contacto_exito"))
    else:
        form = ContactFormModelForm()

    return render(request, "web/contacto.html", {"form": form})
