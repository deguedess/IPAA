import datetime
from Polls.admin import Carteira
from Polls.models import Perfil, Respostas_usuario, Simulacao_cenarios, Usuario
from Portfolio.models import Carteiras, Hist_alt_carteira, Acao

# Metodo para buscar as respostas do usuario e definir o perfil


class calculaPortfolio():

    def verificaPerfil(userid):

        pontos = 0
        for resposta in Respostas_usuario.objects.filter(usuario_id=userid):
            pontos += resposta.resposta.pontuacao

        ptos = int(pontos)

        try:
            perf = Perfil.objects.get(
                peso_inicial__lte=ptos, peso_final__gte=ptos)

        except Exception as e:
            perf = 'Perfil Não Encontrado'
            print(e)

        return perf


# metodo para criação da carteira inicial

    def criaCarteira(userid, tipoGrupo, acoes):
        cart = Carteiras()
        cart.usuario = Usuario.objects.get(pk=userid)
        cart.tipo_grupo = tipoGrupo
        cart.nome = 'Carteira ' + 'Automática' if tipoGrupo == 0 else 'Manual'
        cart.save()
        cart.acoes.set(acoes)
        cart.save()
        return cart

    def salvaPortfolio(carteira, acoesSelected):
        # se for manual
        if carteira.tipo_grupo == 1:
            calculaPortfolio.registraAlteracoes(
                acoesSelected, carteira, 'C', False, False, None, None)
        else:
            # aqui o bixo pega, valida o que o usuario alterou antes de salvar
            calculaPortfolio.registraAlteracoes(
                acoesSelected, carteira, 'C', False, False, None, None)

# metodo para salvar alteração de carteira
    def registraAlteracao(acao, carteira, oper, recIA, segRec, motivo, simulacao):
        hist = Hist_alt_carteira()
        hist.acao = acao
        hist.carteira = carteira
        hist.data_alt = datetime.datetime.now()
        hist.operacao = oper
        hist.recomendacao_ia = recIA
        hist.seguiu_recomendacao = segRec
        hist.motivo = motivo
        hist.simulacao = Simulacao_cenarios.objects.get(
            pk=1) if simulacao == None else simulacao
        hist.save()

    def registraAlteracoes(acoes, carteira, oper, recIA, segRec, motivo, simulacao):
        for acao in acoes:
            calculaPortfolio.registraAlteracao(
                acao, carteira, oper, recIA, segRec, motivo, simulacao)


# metodo para verificar quais as ações se encaixam no perfil

    def calculaAcoes():
        pass
