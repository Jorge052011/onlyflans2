from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, View
from web.models import Producto  # tu modelo vive en la app 'web'
from .cart import Cart
from .forms import AddToCartForm

class CartDetailView(TemplateView):
    template_name = "cart/cart_detail.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cart"] = Cart(self.request)
        return ctx

class CartAddView(FormView):
    form_class = AddToCartForm
    success_url = reverse_lazy("cart_detail")
    template_name = "cart/cart_detail.html"  # no se usa realmente (posteas desde detalle)

    def form_valid(self, form):
        product = get_object_or_404(Producto, pk=self.kwargs["pk"])
        qty = form.cleaned_data["quantity"]
        cart = Cart(self.request)
        cart.add(product, quantity=qty)
        return super().form_valid(form)

class CartRemoveView(View):
    success_url = reverse_lazy("cart_detail")
    def post(self, request, pk):
        product = get_object_or_404(Producto, pk=pk)
        Cart(request).remove(product)
        return redirect(self.success_url)
