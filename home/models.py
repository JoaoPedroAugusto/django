from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=20, unique=True)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)
    texto = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nome
    

class MyFile(models.Model):
    file = models.FileField(upload_to='midia/img')  # Correção do caminho
    tittle = models.CharField(max_length=20)  # Correção do nome do campo

    def __str__(self):
        return self.title
