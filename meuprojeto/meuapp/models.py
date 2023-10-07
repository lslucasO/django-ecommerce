from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    cliente = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=255, null=True)
    preco = models.FloatField()
    has_product = models.BooleanField(default=False, null=True, blank=False)
    
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=)
    data_pedido = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    id_transacao = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id_transacao)