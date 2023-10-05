from django.db import models

# Create your models here.
class Associado(models.Model):
    id_associado = models.AutoField(primary_key=True)
    cpf = models.IntegerField()
    email = models.EmailField(help_text=200)
    