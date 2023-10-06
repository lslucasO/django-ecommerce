from django.shortcuts import render
from .models import Associado

# Create your views here.
rooms = [
    {'id': 2, 'name': 'produtos'},
    {'id': 3, 'name': 'ofertas'},
    {'id': 4, 'name': 'carrinho'},
    {'id': 5, 'name': 'contato'},
    {'id': 6, 'name': 'associados'}
]

produtos = [
    {'nome': 'arroz'},
    {'nome': 'arroz'},
    {'nome': 'arroz'},
    {'nome': 'arroz'},
    {'nome': 'arroz'}
]
    


def index(request):
    return render(request, 'html/index.html', {'rooms': rooms})

def produtos(request):
    
    return render(request, 'html/produtos.html', {'produtos': produtos})

def ofertas(request):
    return render(request, 'html/ofertas.html', {'rooms': rooms})

def associados(request):
    novo_associado = Associado()
    novo_associado.cpf = request.POST.get('cpf')
    novo_associado.email = request.POST.get('email')
    novo_associado.save()
    
    associados = {
        'associados': Associado.objects.all()
    }
    
    return render(request, 'html/associados.html', associados)   
