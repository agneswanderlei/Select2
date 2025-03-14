from django.db import models

class Estados(models.Model):
    name = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.uf} - {self.name}'

class Pessoas(models.Model):
    name = models.CharField(max_length=100)  # Nome da pessoa
    estados = models.ManyToManyField(Estados)  # Relacionamento de muitos-para-muitos com Estados

    def __str__(self):
        return self.name
