from django.db import models

# Create your models here.

#
# Motivos de alteração na carteira


class Motivos(models.Model):
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


class Profissoes(models.Model):
    nome = models.CharField(
        max_length=100, help_text='Informe o nome da profissão')

    def __str__(self):
        return self.nome

#
# Ações


class Acoes(models.Model):
    codigo = models.CharField(
        max_length=10, help_text='Informe o código da ação')

    nome = models.CharField(
        max_length=100, help_text='Informe o nome da ação')

    def __str__(self):
        return self.codigo


#
# Perfis


class Perfis(models.Model):
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


class Perguntas(models.Model):
    pergunta = models.CharField(
        max_length=500, help_text='Informe a pergunta')

    status = models.BooleanField()

    def __str__(self):
        return self.pergunta


#
# Respostas


class Respostas(models.Model):

    pergunta = models.ForeignKey(
        'Perguntas', on_delete=models.CASCADE, null=False)

    resposta = models.CharField(
        max_length=200, help_text='Informe a resposta')

    sequencia = models.IntegerField()

    pontuacao = models.DecimalField(
        max_digits=6, decimal_places=4)

    def __str__(self):
        return self.resposta


#
# Usuario


class Usuarios(models.Model):

    idade = models.IntegerField()

    genero = models.IntegerField()

    grau_instrucao = models.ForeignKey(
        'Grau_Instrucao', on_delete=models.SET_NULL, null=True)

    profissao = models.ForeignKey(
        'Profissoes', on_delete=models.SET_NULL, null=True)

    data_cadastro = models.DateTimeField(
        null=False, blank=False, auto_now_add=True)

    perfil = models.ForeignKey(
        'Perfis', on_delete=models.SET_NULL, null=True)

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
        'Respostas', on_delete=models.RESTRICT, null=False)

    usuario = models.ForeignKey(
        'Usuarios', on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return self.resposta
