from django.db import models

from Polls.models import Acoes

# Create your models here.
#
# Simulação


class Simulacoes(models.Model):
    nome = models.CharField(
        max_length=100, help_text='Informe o nome da simulação')

    descricao = models.CharField(
        max_length=300, help_text='Informe a descrição da simulação', null=True)

    data_inicial = models.DateTimeField(
        null=False, blank=False)

    data_final = models.DateTimeField(
        null=False, blank=False)

    def __str__(self):
        return self.nome


#
# Ações da simulação


class Simulacao_acao(models.Model):
    acao = models.ForeignKey(
        Acoes, on_delete=models.CASCADE, null=False)

    simulacao = models.ForeignKey(
        Simulacoes, on_delete=models.CASCADE, null=False)

    valor_ant = models.DecimalField(
        max_digits=7, decimal_places=2)

    valor_novo = models.DecimalField(
        max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome
