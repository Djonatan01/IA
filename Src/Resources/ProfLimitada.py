from Src.Models.ListaDEnc import lista
from Src.Util.functions import sucessores

class ProfLimitada(object):
    def __init__(self, inicio, fim, mapa, limite, portalMap):
        self.inicio = inicio
        self.fim = fim
        self.mapa = mapa
        self.limite = limite
        self.portalMap = portalMap

    # BUSCA EM PROFUNDIDADE LIMITADA
    def make(self):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(self.inicio,0,None)
        l2.insereUltimo(self.inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(self.inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()

            if atual.nivel< self.limite:
                #ind = nos.index(atual.estado)

                filhos = sucessores(atual.estado, self.mapa, self.portalMap)

                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:

                    # pressuponho que não foi visitado
                    flag = True

                    # controle de nós repetidos
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.nivel+1
                            break

                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado.append(linha)

                        # verifica se é o objetivo
                        if novo == self.fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            return caminho

        return "error"