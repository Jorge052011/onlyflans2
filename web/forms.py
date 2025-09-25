
from .models import ContactForm
from django import forms

class ContactFormForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo electrónico")
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)




class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['nombre', 'email', 'mensaje']