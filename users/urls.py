


from django.urls import path
from .views import Login, Registro, Logout

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", Registro.as_view() , name = "register"),
    path("logout/", Logout.as_view() , name = "logout")
]


