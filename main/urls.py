from django.urls import path

from . import views # importa a views a partir do diretório que estamos

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
]