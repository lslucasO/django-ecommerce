
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from meuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('produtos/', views.produtos, name="produtos"),
    path('ofertas/', views.ofertas, name="ofertas"),
    path('carrinho/', views.carrinho, name="carrinho"),
    path('compra/', views.compra, name="compra")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)