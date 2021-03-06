from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "usuario"

urlpatterns = [
    path("cadastro", views.cadastro, name="cadastro"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
]
