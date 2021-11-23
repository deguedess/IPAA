from django.db import models

from Polls.models import Acoes, Motivos, Usuarios
from Simulation.models import Simulacoes

# Create your models here.
#
# Carteira


class Carteiras(models.Model):
    nome = models.CharField(
        max_length=100, help_text='Informe o nome da carteira')

    usuario = models.ForeignKey(
        Usuarios, on_delete=models.CASCADE, null=False)

    tipo_grupo = models.IntegerField()

    acoes = models.ManyToManyField(
        Acoes, help_text='Informe as ações da carteira')

    def __str__(self):
        return self.nome


#
# Historico da carteira


class Hist_alt_carteira(models.Model):
    acao = models.ForeignKey(
        Acoes, on_delete=models.CASCADE, null=False)

    carteira = models.ForeignKey(
        Carteiras, on_delete=models.CASCADE, null=False)

    data_alt = models.DateTimeField(
        null=False, blank=False, auto_now_add=True)

    operacao = models.IntegerField()  # 0 compra, 1 venda

    recomendacao_ia = models.BooleanField()

    seguiu_recomendacao = models.BooleanField()

    motivo = models.ForeignKey(
        Motivos, on_delete=models.CASCADE, null=False)

    simulacao = models.ForeignKey(
        Simulacoes, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.acao
