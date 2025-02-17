from django.db import models


# Create your models here
class Order(models.Model):
    nome_pedido = models.CharField(max_length=300)
    descricao = models.CharField(max_length=200)
    data = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nome_pedido
    