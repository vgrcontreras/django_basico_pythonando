from django.urls import path, include
from . import views

urlpatterns = [
    path('ver_produtos/', views.ver_produtos, name='ver_produtos'),
    path('inserir_produtos/', views.inserir_produtos, name='inserir_produtos')
]
