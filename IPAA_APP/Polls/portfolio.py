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

            if (cart.tipo_grupo == 0):
                calculaPortfolio.registraAlteracoes(
                    acoes, cart, 'C', True, True, None, None)

        return cart

    def verificaCarteira(userid):
        cart = Carteiras.objects.filter(usuario_id=userid)

        if (cart.count() == 0):
            return None
        else:
            return cart[0]

    def salvaHistoricoCarteiraManual(cart, acoesSel):

        acoesCart = cart.acoes.all()

        # verificar as acoes selecionadas
        for acSel in acoesSel:
            # Se a ação selecionada nao estiver na carteira, registra a alteração
            if (acSel not in acoesCart):
                calculaPortfolio.registraAlteracao(
                    acSel, cart, 'C', False, False, None, None)

        # verifica as ações na carteira
        for acCat in acoesCart:
            if (acCat not in acoesSel):
                calculaPortfolio.registraAlteracao(
                    acCat, cart, 'V', False, False, None, None)

    def salvaHistoricoCarteiraIA(cart, acoesSel, acoesRec):
        acoesCart = cart.acoes.all()

        # verifica as acoes selecionadas = COMPRAS
        for acSel in acoesSel:
            # se a ação nao estiver na carteira, houve alteração, nesse caso ADICIONADA
            if (acSel not in acoesCart):
                # verifica se a alteração foi recomendada ou nao
                if (acSel in acoesRec):
                    calculaPortfolio.registraAlteracao(
                        acSel, cart, 'C', True, True, None, None)
                else:  # se nao for recomendação
                    calculaPortfolio.registraAlteracao(
                        acSel, cart, 'C', False, False, None, None)

        # verificar as ações na carteira = VENDAS
        for acCart in acoesCart:
            # se a ação nao estiver na selecionadas, houve alteração, nesse caso foi REMOVIDA
            if (acCart not in acoesSel):
                # verificar se a venda foi recomendada ou nao
                if (acCart in acoesRec):
                    calculaPortfolio.registraAlteracao(
                        acCart, cart, 'V', False, False, None, None)
                else:  # se nao for recomendação
                    calculaPortfolio.registraAlteracao(
                        acCart, cart, 'V', True, True, None, None)

         # Verifica as RECOMENDADAS
        for acRec in acoesRec:
            if (acRec not in acoesSel):
                calculaPortfolio.registraAlteracao(
                    acRec, cart, 'C', True, False, None, None)

    def salvaPortfolio(carteira, acoesSelected, recomended):

        print("1")
        print(carteira.acoes.all())
        print("2")
        print(acoesSelected)
        print("3")
        print(recomended)

        if (carteira.tipo_grupo == 0):
            calculaPortfolio.salvaHistoricoCarteiraIA(
                carteira, acoesSelected, recomended)
        else:
            calculaPortfolio.salvaHistoricoCarteiraManual(
                carteira, acoesSelected)

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
