class No(object):
    def __init__(self, pai=None, x=0, estado=None, nivel=None, anterior=None,  proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.nivel     = nivel
        self.anterior  = anterior
        self.proximo   = proximo
        self.x         = x
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, estado, nivel, pai):
        novo_no = No(pai, estado, nivel, 0, 0)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, estado, nivel, pai):

        novo_no = No(pai, estado, nivel, 0, 0)

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
    def amplitude(self, inicio, fim, mapa,n,m):
    #def amplitude(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0)
        l2.insereUltimo(inicio,0,0)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()

            filhos = sucessores(atual,mapa,n,m)

            print(f"Dimensão do mapa: {altura} x {largura}")
            y1 = int(atual.x[0])
            x1 = int(atual.x[1])

            mapa[y1][x1] = 5
            # Exemplo de uso
            imprime_matriz(mapa)

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
                    l1.insereUltimo(novo, atual.nivel + 1, atual.x)
                    l2.insereUltimo(novo, atual.nivel + 1, atual.x)

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
def sucessores(atual, mapa, n, m):
    f = []
    xa = int(atual.x[1])
    ya = int(atual.x[0])

    if xa + 1 != n:
        if mapa[ya][xa + 1] == 1 or mapa[ya][xa + 1] == 5:
            f.append([str(ya), str(xa + 1)])
    if xa != 0:
        if mapa[ya][xa - 1] == 1 or mapa[ya][xa - 1] == 5:
            f.append([str(ya), str(xa - 1)])
    if ya + 1 != m:
        if mapa[ya + 1][xa] == 1 or mapa[ya + 1][xa] == 5:
            f.append([str(ya + 1), str(xa)])
    if ya != 0:
        if mapa[ya - 1][xa] == 1 or mapa[ya - 1][xa] == 5:
            f.append([str(ya - 1), str(xa)])

    return f

# Função para verificar se as coordenadas estão dentro dos limites do mapa
def coordenadas_dentro_limites(x, y, mapa):
    return 0 <= x <= len(mapa) and 0 <= y <= len(mapa[0])

# Função para verificar se as coordenadas correspondem a um valor válido no mapa
def coordenadas_valido_no_mapa(x, y, mapa):
    return mapa[x - 1][y - 1] in [0, 1] # Ajuste os valores [1, 2] conforme necessário


def Gera_Problema(arquivo):
    with open(arquivo, "r") as f:
        mapa = []
        for linha in f:
            # Remove espaços em branco e quebras de linha
            linha = linha.strip()
            # Divide a linha em uma lista de caracteres (1s e 2s)
            linha_convertida = list(map(int, linha))
            # Adiciona a linha convertida como uma nova lista na matriz
            mapa.append(linha_convertida)
    return mapa

# PROGRAMA PRINCIPAL
#nos, grafo = Gera_Problema("romenia.txt")
mapa = Gera_Problema("mapa.txt")

# Obtém o número de linhas (altura) do mapa
altura = len(mapa)

# Obtém o número de colunas (largura) do mapa assumindo que todas as linhas têm o mesmo número de elementos
largura = len(mapa[0]) if mapa else 0

# Imprime a dimensão do mapa
print(f"Dimensão do mapa: {altura} x {largura}")

def imprime_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(elemento) for elemento in linha))

# Exemplo de uso
imprime_matriz(mapa)


sol = busca()
caminho = []

#origem  = input("\n\nOrigem (x,y): ").split(',')
#destino = input("Destino (x,y): ").split(',')

origem  = ('0,0').split(',')
destino = ('9,9').split(',')

origem_coordenadas = [int(coord) for coord in origem]
destino_coordenadas = [int(coord) for coord in destino]

if not (coordenadas_dentro_limites(*origem_coordenadas, mapa) and coordenadas_dentro_limites(*destino_coordenadas, mapa)):
    print("Coordenadas não estão na lista")
elif not (coordenadas_valido_no_mapa(*origem_coordenadas, mapa) and coordenadas_valido_no_mapa(*destino_coordenadas, mapa)):
    print("Coordenadas não correspondem a um valor válido no mapa")
else:
    #caminho = sol.amplitude(origem,destino)
    caminho = sol.amplitude(origem,destino,mapa,altura,largura)
    print("\n*****AMPLITUDE*****\n",caminho)
    if caminho!="caminho não encontrado":
        print("\nCusto: ",len(caminho)-1)
