import numpy as np
import random as rd

class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, 
                valor2=None, anterior=None, proximo=None):
        # controle da árvore de busca
        self.pai       = pai
        # indica o nó do grafo
        self.estado    = estado
        # função de avaliação f(n) do método
        self.valor1    = valor1        
        # custo do caminho da origem até o nó atual
        self.valor2    = valor2     
        # controle da lista encadeada
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NA LISTA MANTENDO A ORDENAÇÃO
    def inserePos_X(self, s, v1, v2, p):
        
        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual

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

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            linha = []
            linha.append(aux.estado)
            linha.append(aux.valor1)            
            str.append(linha)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    def exibeArvore1(self,s):

        atual = self.head
        while atual.estado != s:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def exibeArvore2(self, s, v1):
        
        atual = self.tail
        
        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior
        
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

class busca(object):
    
    def custo_uniforme(self, inicio, fim):  
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2 # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1, v2, atual)
                    l2.insereUltimo(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      
    
    def greedy(self, inicio, fim, h):  
        ind_f = nos.index(fim)
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                ind_n = nos.index(novo[0])
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = h[ind_f][ind_n] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1, v2, atual)
                    l2.insereUltimo(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"
    
    def a_estrela(self, inicio, fim, h):  
        ind_f = nos.index(fim)
        
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                ind_n = nos.index(novo[0])
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2 + h[ind_f][ind_n] # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1, v2, atual)
                    l2.insereUltimo(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"

    def aia_estrela(self, inicio, fim, h, limite, lim_max):  
        ind_f = nos.index(fim)
        
        while limite<=lim_max:
            
            lim_acima = []
            
            l1 = lista()
            l2 = lista()
            visitado = []
            l1.insereUltimo(inicio,0,0,None)
            l2.insereUltimo(inicio,0,0,None)
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
            
            while l1.vazio() == False:
                atual = l1.deletaPrimeiro()
                
                if atual.estado == fim:
                    caminho = []
                    caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                    #print("Cópia da árvore:\n",l2.exibeLista())
                    #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                    return caminho[::-1], atual.valor2
            
                ind = nos.index(atual.estado)
                for novo in grafo[ind]:
                    
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    ind_n = nos.index(novo[0])
                    v2 = atual.valor2 + novo[1]  # custo do caminho
                    v1 = v2 + h[ind_f][ind_n] # f1(n)
                    
                    if v1<=limite:
                        flag1 = True
                        flag2 = True
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo[0]:
                                if visitado[j][1]<=v2:
                                    flag1 = False
                                else:
                                    visitado[j][1]=v2
                                    flag2 = False
                                break
            
                        if flag1:
                            l1.inserePos_X(novo[0], v1, v2, atual)
                            l2.insereUltimo(novo[0], v1, v2, atual)
                            if flag2:
                                linha = []
                                linha.append(novo[0])
                                linha.append(v2)
                                visitado.append(linha)
                    else:
                        lim_acima.append(v1)
            limite = sum(lim_acima)/len(lim_acima)
            print(limite)
                        
        return "Caminho não encontrado", 0    

    
def gera_H(nos,n):
    aux = busca()
    h = np.zeros((n,n),int)
    i = 0
    for no_destino in nos:
        j = 0
        for no_origem in nos:
            if no_origem != no_destino:
                cam, v  = aux.custo_uniforme(no_origem, no_destino)
                h[i][j] = v*rd.uniform(0.8,1)
            j += 1
        i += 1
    return h

nos = ["ARAD","BUCARESTE","CRAIOVA","DOBRETA","EFORIE",
       "FAGARAS","GIURGIU","HIRSOVA","IASI","LUGOJ","MEHADIA",
       "NEAMT","ORADEA","PITESTI","RIMINCU VILCEA","SIBIU",
       "TIMISOARA","URZICENI","VASLUI","ZERIND"]

grafo = [[["ZERIND",75], ["TIMISOARA",118], ["SIBIU",140]],
         [["URZICENI",85], ["PITESTI",101], ["GIURGIU",90],["FAGARAS",211]], 
         [["RIMINCU VILCEA",146], ["PITESTI",138], ["DOBRETA",120]], 
         [["MEHADIA",75], ["CRAIOVA",120]], 
         [["HIRSOVA",86]],
         [["SIBIU",99], ["BUCARESTE",211]], 
         [["BUCARESTE",90]], 
         [["URZICENI",98], ["EFORIE",86]], 
         [["VASLUI",92], ["NEAMT",87]],
         [["TIMISOARA",111],["MEHADIA",70]], 
         [["LUGOJ",70], ["DOBRETA",75]], 
         [["IASI",87]], 
         [["ZERIND",71], ["SIBIU",151]],
         [["RIMINCU VILCEA",97], ["CRAIOVA",138], ["BUCARESTE",101]], 
         [["SIBIU",80], ["PITESTI",97], ["CRAIOVA",146]], 
         [["RIMINCU VILCEA",80], ["ORADEA",151], ["FAGARAS",99], ["ARAD",140]], 
         [["LUGOJ",111], ["ARAD",118]],
         [["VASLUI",142], ["HIRSOVA",98], ["BUCARESTE",85]], 
         [["URZICENI",142], ["IASI",92]], 
         [["ORADEA",71], ["ARAD",75]]
        ]
# HEURISTICA SERVE SOMENTE PARA DESTINO BUCARESTE
sol = busca()
caminho = []
# gera a matriz de heurística
h = gera_H(nos,len(nos))
h[1] = [366,0,160,242,161,178,77,151,226,244,241,234,380,98,193,253,329,80,199,374]
print(h)


print("**** LISTA DE NÓS ****\n")
print(nos)

inicio = input("\nDigite o nó de partida: ")
final  = input("Digite o nó de chegada: ")
print("\n")

inicio = inicio.upper()
final  = final.upper()

ind_i = nos.index(final)
ind_f = nos.index(inicio)

"""
caminho, custo = sol.custo_uniforme(inicio,final)
print("Custo Uniforme: ",caminho[::-1],"\nCusto do Caminho: ",custo)

caminho, custo = sol.greedy(inicio,final,h)
print("\nGreedy: ",caminho[::-1],"\nCusto do caminho: ",custo)

caminho, custo = sol.a_estrela(inicio,final,h)
print("\nA_estrela: ",caminho[::-1],"\nCusto do caminho: ",custo)
"""
limite = h[ind_i][ind_f]
lim_max = 430
caminho, custo = sol.aia_estrela(inicio,final,h,limite,lim_max)
print("\nAIA_estrela: ",caminho[::1],"\nCusto do caminho: ",custo)
