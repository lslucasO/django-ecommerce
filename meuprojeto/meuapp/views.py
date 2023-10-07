from django.shortcuts import render
from .models import Associado

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

def associados(request):
    novo_associado = Associado()
    novo_associado.cpf = request.POST.get('cpf')
    novo_associado.email = request.POST.get('email')
    novo_associado.save()
    
    associados = {
        'associados': Associado.objects.all()
    }
    
    return render(request, 'html/associados.html', associados)   
