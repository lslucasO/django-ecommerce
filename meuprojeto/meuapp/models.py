from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    cliente = models.OneToOneField(User, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.nome