from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def produtos(request):
    return render(request, 'html/produtos.html', )

def ofertas(request):
    return render(request, 'html/ofertas.html')

def carrinho(request):
    return render(request, 'html/carrinho.html')

def compra(request):
    return render(request, 'html/compra.html')
