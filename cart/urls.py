

from django.urls import path
from .views import CartDetailView, CartAddView, CartRemoveView

urlpatterns = [
    path("", CartDetailView.as_view(), name="cart_detail"),
    path("agregar/<int:pk>/", CartAddView.as_view(), name="cart_add"),
    path("eliminar/<int:pk>/", CartRemoveView.as_view(), name="cart_remove"),
]
