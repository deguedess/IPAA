from django.contrib import admin

from Polls.models import Acao, Grau_Instrucao, Motivo, Perfil, Pergunta, Profissao, Resposta, Simulacao_cenarios


# Register your models here.


@admin.register(Motivo)
class MotivoAdmin(admin.ModelAdmin):
    pass


@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    pass


@admin.register(Grau_Instrucao)
class Grau_InstrucaoAdmin(admin.ModelAdmin):
    pass


@admin.register(Profissao)
class ProfissaoAdmin(admin.ModelAdmin):
    pass


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'status')


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'resposta', 'sequencia', 'pontuacao')
    list_filter = ('pergunta', 'pontuacao')
    fields = ['pergunta', 'resposta', ('sequencia', 'pontuacao')]


@admin.register(Simulacao_cenarios)
class PerfilAdmin(admin.ModelAdmin):
    pass
