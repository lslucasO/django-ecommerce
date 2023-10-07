from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'html/produtos.html', context=context)

def ofertas(request):
    return render(request, 'html/ofertas.html')

def carrinho(request):
    carrinhos = ItemPedido.objects.all()
    context = {'carrinhos': carrinhos}
    return render(request, 'html/carrinho.html', context=context)

def compra(request):
    return render(request, 'html/compra.html')
