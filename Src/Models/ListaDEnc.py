from Src.Models.node import No,No_od

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

class lista_od(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No_od(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No_od(p, s, v1, v2, None, None)

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
                    novo_no = No_od(p,s,v1,v2,None,None)
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