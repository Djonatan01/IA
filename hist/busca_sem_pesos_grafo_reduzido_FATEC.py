class No(object):
    def __init__(self, pai=None, estado=None, nivel=None, anterior=None,  proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.nivel     = nivel
        self.anterior  = anterior
        self.proximo   = proximo

class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, st, ni, p):
        novo_no = No(p, st, ni, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, st, ni, p):

        novo_no = No(p, st, ni, None, None)

        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
            self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    # RETORNA O PRIMEIRO DA LISTA
    def primeiro(self):
        return self.head

    # RETORNA O ÚLTIMO DA LISTA
    def ultimo(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA
    def vazio(self):
        if self.head is None:
            return True
        else:
            return False

    # EXIBE O CONTEÚDO DA LISTA
    def exibeLista(self):

        aux = self.head
        str1 = []
        while aux != None:
            temp = []
            temp.append(aux.estado)
            temp.append(aux.nivel)
            str1.append(temp)
            aux = aux.proximo

        return str1

    # EXIBE O CAMINHO ENCONTRADO
    def exibeCaminho(self):

        atual = self.tail
        caminho = []

        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai

        caminho.append(atual.estado)
        caminho = caminho[::-1]
        return caminho

    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
    def exibeCaminho1(self,valor):

        atual = self.head
        while atual.estado != valor:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

class busca(object):

    # BUSCA EM AMPLITUDE
    #def amplitude(self, inicio, fim, mapa,n,m):
    def amplitude(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()

            ind = nos.index(atual.estado)

            # filhos = sucessores(atual,mapa,n,m)
            # varre todos as conexões dentro do grafo a partir de atual
            #for novo in filhos:
            for novo in grafo[ind][::1]:
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
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        print("\nFila:\n",l1.exibeLista())
                        print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"


def Gera_Problema(arquivo):
    f = open(arquivo,"r")

    i=0
    nos = []
    grafo = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        if i==0:
            nos = str1
        else:
            grafo.append(str1)
        i += 1

    return nos, grafo

# PROGRAMA PRINCIPAL
nos, grafo = Gera_Problema("romenia.txt")
# mapa = GeraProblema("mapa.txt)

print("===> Lista de nos:\n\n",nos )

sol = busca()
caminho = []

origem  = input("\n\nOrigem: ").upper()
destino = input("Destino: ").upper()

if origem not in nos or destino not in nos:
    print("Cidade não está na lista")
else:
    caminho = sol.amplitude(origem,destino)
    #caminho = sol.amplitude(origem,destino,mapa)
    print("\n*****AMPLITUDE*****\n",caminho)
    if caminho!="caminho não encontrado":
        print("\nCusto: ",len(caminho)-1)
