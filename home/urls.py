from django.urls import path
from django_distill import distill_path
from . import views


# função que retorna parâmetros de URL (aqui só uma rota sem parâmetro)
def get_home():
    yield {}


urlpatterns = [
    # rota normal (útil pra debug local)
    path('', views.home, name='home'),
    # rota para distill
    distill_path('', views.home, name='home',
                 distill_func=get_home,
                 distill_file='index.html'),
]
