from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Sobre Nos'},
    {'id': 2, 'name': 'Produtos'},
    {'id': 3, 'name': 'Ofertas'},
    {'id': 4, 'name': 'Carrinho'},
    {'id': 5, 'name': 'Contato'}
]

def index(request):
    return render(request, 'html/index.html', {'rooms': rooms})

def produtos (request, pk):
    return render(request, 'html/produtos.html')