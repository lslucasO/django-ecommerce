from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 2, 'name': 'produtos'},
    {'id': 3, 'name': 'ofertas'},
    {'id': 4, 'name': 'carrinho'},
    {'id': 5, 'name': 'contato'}
]

def index(request):
    return render(request, 'html/index.html', {'rooms': rooms})

def produtos(request):
    return render(request, 'html/produtos.html', {'rooms': rooms})

def ofertas(request):
    return render(request, 'html/ofertas.html', {'rooms': rooms})