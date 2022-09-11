from django.urls import path

from . import views # importa a views a partir do diretório que estamos

urlpatterns = [
path("<str:name>", views.index, name="index")
]