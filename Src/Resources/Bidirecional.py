from Src.Models.ListaDEnc import lista
from Src.Util.functions import sucessores


class Bidirecional(object):
    def __init__(self, inicio, fim, mapa, portalMap):
        self.inicio = inicio
        self.fim = fim
        self.mapa = mapa
        self.portalMap = portalMap

    # BUSCA BIDIRECIONAL
    def make(self):
        # Primeiro Amplitude"
        # Manipular a FILA para a busca
        l1 = lista()
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # Segundo Amplitude"
        # Manipular a FILA para a busca
        l3 = lista()
        # cópia para apresentar o caminho (somente inserção)
        l4 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(self.inicio,0,None)
        l2.insereUltimo(self.inicio,0,None)

        l3.insereUltimo(self.fim,0,None)
        l4.insereUltimo(self.fim,0,None)

        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(self.inicio)
        linha.append(0)
        visitado1.append(linha)

        visitado2 = []
        linha = []
        linha.append(self.fim)
        linha.append(0)
        visitado2.append(linha)

        ni = 0
        while l1.vazio()==False or l3.vazio()==False:

            while l1.vazio() == False:

                # para ir para o próximo amplitude
                if ni!=l1.primeiro().nivel:
                    break

                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()

                filhos = sucessores(atual.estado, self.mapa, self.portalMap)
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
                    # pressuponho que não foi visitado
                    flag = True

                    # controle de nós repetidos
                    for j in range(len(visitado1)):
                        if visitado1[j][0]==novo:
                            if visitado1[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado1[j][1]=atual.nivel+1
                            break

                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado1.append(linha)

                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado2)):
                            if visitado2[j][0]==novo:
                                flag = True
                                break

                        if flag:
                            caminho = []
                            #print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho

            while l3.vazio() == False:

                # para ir para o próximo amplitude
                if ni!= l3.primeiro().nivel:
                    break

                # remove o primeiro da fila
                atual = l3.deletaPrimeiro()

                filhos = sucessores(atual.estado, self.mapa, self.portalMap)

                for novo in filhos:
                    # pressuponho que não foi visitado
                    flag = True

                    # controle de nós repetidos
                    for j in range(len(visitado2)):
                        if visitado2[j][0]==novo:
                            if visitado2[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado2[j][1]=atual.nivel+1
                            break

                    # se não foi visitado inclui na fila
                    if flag:
                        l3.insereUltimo(novo, atual.nivel + 1, atual)
                        l4.insereUltimo(novo, atual.nivel + 1, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado2.append(linha)

                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado1)):
                            if visitado1[j][0]==novo:
                                flag = True
                                break

                        if flag:
                            caminho = []
                            #print("Fila:\n",l3.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]

            ni += 1

        return "error"
