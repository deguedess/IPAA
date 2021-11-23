from typing import Reversible
from django.db import models

# Create your models here.

#
# Motivos de alteração na carteira


class Motivo(models.Model):
    nome = models.CharField(
        max_length=100, help_text='Informe o nome do motivo')

    def __str__(self):
        return self.nome

#
# Grau de instrução


class Grau_Instrucao(models.Model):
    nome = models.CharField(
        max_length=100, help_text='Informe o grau de instrução')

    def __str__(self):
        return self.nome

#
# Profissão


class Profissao(models.Model):
    nome = models.CharField(
        max_length=100, help_text='Informe o nome da profissão')

    def __str__(self):
        return self.nome

#
# Ações


class Acao(models.Model):
    codigo = models.CharField(
        max_length=10, help_text='Informe o código da ação')

    nome = models.CharField(
        max_length=100, help_text='Informe o nome da ação')

    def __str__(self):
        return self.codigo


#
# Perfis


class Perfil(models.Model):
    nome = models.CharField(
        max_length=100, help_text='Informe o nome do perfil')

    peso_inicial = models.IntegerField()

    peso_final = models.IntegerField()

    tipo = models.CharField(
        max_length=50, help_text='Informe o tipo de perfil')

    def __str__(self):
        return self.nome


#
# Perguntas


class Pergunta(models.Model):
    pergunta = models.CharField(
        max_length=500, help_text='Informe a pergunta')

    status = models.BooleanField()

    def __str__(self):
        return self.pergunta

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return Reversible('poll-detail', args=[str(self.id)])


#
# Respostas


class Resposta(models.Model):

    pergunta = models.ForeignKey(
        Pergunta, on_delete=models.CASCADE, null=False)

    resposta = models.CharField(
        max_length=200, help_text='Informe a resposta')

    sequencia = models.IntegerField()

    pontuacao = models.DecimalField(
        max_digits=6, decimal_places=4)

    def __str__(self):
        return self.resposta


#
# Usuario


class Usuario(models.Model):

    idade = models.IntegerField()

    sexo = (
        ('m', 'Masculino'),
        ('f', 'Femenino'),
    )

    genero = models.CharField(
        max_length=1,
        choices=sexo,
        blank=True,
        help_text='Gênero',
    )

    grau_instrucao = models.ForeignKey(
        Grau_Instrucao, on_delete=models.SET_NULL, null=True)

    profissao = models.ForeignKey(
        Profissao, on_delete=models.SET_NULL, null=True)

    data_cadastro = models.DateTimeField(
        null=False, blank=False, auto_now_add=True)

    perfil = models.ForeignKey(
        Perfil, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.idade)


#
# Respostas_usuario


class Respostas_usuario(models.Model):

    data_inicial = models.DateTimeField(
        null=False, blank=False)

    data_final = models.DateTimeField(
        null=False, blank=False, auto_now_add=True)

    resposta = models.ForeignKey(
        Resposta, on_delete=models.RESTRICT, null=False)

    usuario = models.ForeignKey(
        Usuario, on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return self.resposta


# Simulação


class Simulacao_cenarios(models.Model):
    nome = models.CharField(
        max_length=100, help_text='Informe o nome da simulação')

    descricao = models.CharField(
        max_length=300, help_text='Informe a descrição da simulação', null=True)

    data_ini = models.DateField(
        null=False, blank=False)

    data_fim = models.DateField(
        null=False, blank=False)

    def __str__(self):
        return self.nome
