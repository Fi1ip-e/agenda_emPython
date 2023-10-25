from django.db import models

# Create your models here.

class TbAgenda(models.Model):
    
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=100)
    contato = models.CharField('Contato', max_length=100)