from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=20, unique=True)
    idade = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nome
    

class MyFile(models.Model):
    file = models.FileField(upload_to='midia/img')  # Correção do caminho
    tittle = models.CharField(max_length=20)  # Correção do nome do campo

    def __str__(self):
        return self.title
