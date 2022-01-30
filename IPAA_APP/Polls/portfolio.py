import datetime
from Polls.admin import Carteira
from Polls.models import Perfil, Respostas_usuario, Simulacao_cenarios, Usuario, Motivo
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

        cart = calculaPortfolio.verificaCarteira(userid)

        if (cart != None):
            return cart

        cart = Carteiras()
        cart.usuario = Usuario.objects.get(pk=userid)
        cart.tipo_grupo = tipoGrupo
        cart.nome = 'Carteira ' + 'Automática' if tipoGrupo == 0 else 'Manual'
        cart.save()
        if (acoes != None):
            cart.acoes.set(acoes)
            cart.save()
        return cart

    def verificaCarteira(userid):
        cart = Carteiras.objects.filter(usuario_id=userid)

        if (cart.count() == 0):
            return None
        else:
            return cart[0]

    def salvaPortfolio(carteira, acoesSelected, recomended):

        print("1")
        print(carteira.acoes.all())
        print("2")
        print(acoesSelected)
        print("3")
        print(recomended)

        # Passa por todas as ações selecionadas pelo usuario
        for acSel in acoesSelected:

            # se a ação nao estiver na carteira, significa que foi adicionada
            if (acSel not in carteira.acoes.all()):
                if (carteira.tipo_grupo == 1):  # se for 1 é carteira manual
                    recIa = False
                    seguiu = False
                else:
                    if (acSel in recomended):  # se for 0 (IA) verificar se tava na recomendação
                        recIa = True
                        seguiu = True
                    else:
                        recIa = False
                        seguiu = False

                calculaPortfolio.registraAlteracao(
                    acSel, carteira, 'C', recIa, seguiu, None, None)

        # Passa por todas as ações na carteira
        for acCart in carteira.acoes.all():

            # se essa ação nao tiver selecionada foi vendida
            if (acCart not in acoesSelected):
                if (carteira.tipo_grupo == 1):  # se for carteira manual
                    calculaPortfolio.registraAlteracao(
                        acCart, carteira, 'V', False, False, None, None)
                else:
                    if (acCart not in recomended):  # se for 0 (IA) verificar se tava na recomendação
                        calculaPortfolio.registraAlteracao(
                            acCart, carteira, 'V', False, False, None, None)

        if (recomended != None):
            # Verifica agora as recomendações
            for acRec in recomended:
                if (acRec not in acoesSelected):
                    calculaPortfolio.registraAlteracao(
                        acRec, carteira, 'C', True, False, None, None)

        # salva as ações que o usuario aceitou recomendação
        if (carteira.tipo_grupo == 0 and recomended != None):
            for aca in acoesSelected:
                if (aca in recomended):
                    calculaPortfolio.registraAlteracao(
                        acRec, carteira, 'C', True, True, None, None)

        # salva as acoes na carteira
        carteira.acoes.set(acoesSelected)
        carteira.save()
        print('ta salvo')


# metodo para salvar alteração de carteira

    def registraAlteracao(acao, carteira, oper, recIA, segRec, motivo, simulacao):
        hist = Hist_alt_carteira()
        hist.acao = acao
        hist.carteira = carteira
        hist.data_alt = datetime.datetime.now()
        hist.operacao = oper
        hist.recomendacao_ia = recIA
        hist.seguiu_recomendacao = segRec
        hist.motivo = Motivo.objects.get(
            pk=carteira.tipo_grupo+1) if motivo == None else motivo
        hist.simulacao = Simulacao_cenarios.objects.get(
            pk=1) if simulacao == None else simulacao
        hist.save()

    def registraAlteracoes(acoes, carteira, oper, recIA, segRec, motivo, simulacao):
        if (acoes.count() == 0):
            return
        for acao in acoes:
            calculaPortfolio.registraAlteracao(
                acao, carteira, oper, recIA, segRec, motivo, simulacao)


# metodo para verificar quais as ações se encaixam no perfil


    def calculaAcoes():
        pass
