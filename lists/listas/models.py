from django.db import models

# Create your models here.

class Lista(models.Model):
    item = models.CharField(max_length=64)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.item} , {self.quantidade}"