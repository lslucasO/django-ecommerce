
from django.contrib import admin
from django.urls import path
from meuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('produtos/', views.produtos, name="produtos"),
    path('ofertas/', views.ofertas, name="ofertas")
]
