from django.db import models

# Create your models here.
class Pedidos(models.Model):
    nome_pedido = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    data = models.DateField(auto_now=True)
    respondia = models.BooleanField()
     
    def __str__(self):
        return self.name_pedido