from django.db import models

# Create your models here.
class Associado(models.Model):
    id_associado = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255)
    cpf = models.IntegerField()
    