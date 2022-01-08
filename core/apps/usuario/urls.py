from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("cadastro", views.index, name="cadastro"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
]
