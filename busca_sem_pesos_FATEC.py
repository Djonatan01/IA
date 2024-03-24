from ListaDEnc import lista
import funcoes_auxiliares as fa

class busca(object):
    # BUSCA EM AMPLITUDE
    def amplitude(self,inicio,fim,mapa,dim_x,dim_y):

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

            filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)

            # varre todos as conexões dentro do grafo a partir de atual
            # varre todos as conexões dentro de filhos
            for novo in filhos:

                flag = True

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
                        return caminho

        return "caminho não encontrado"

    # BUSCA EM PROFUNDIDADE
    def profundidade(self,inicio,fim,mapa,dim_x,dim_y):

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
            atual = l1.deletaUltimo()

            # Manipulação de Grade de Ocupação
            filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)

            # varre todos as conexões dentro do grafo a partir de atual
            # varre todos as conexões dentro de filhos
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
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("\nFila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"

    # BUSCA EM PROFUNDIDADE LIMITADA
    def prof_limitada(self,inicio,fim,mapa,dim_x,dim_y,limite):

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
            atual = l1.deletaUltimo()

            if atual.nivel<limite:
                #ind = nos.index(atual.estado)

                filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)

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
                        if novo == fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            #print("\nPilha:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho

        caminho = []
        caminho.append("caminho não encontrado")
        return caminho

    # BUSCA EM APROFUNDAMENTO ITERATIVO
    def aprof_iterativo(self,inicio,fim,mapa,dim_x,dim_y,lim_max):
        for limite in range(1,lim_max):
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
                atual = l1.deletaUltimo()

                if atual.nivel<limite:

                    filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)

                    # for novo in filhos:
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
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                #print("\nPilha:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho, limite

        caminho = []
        caminho.append("caminho não encontrado")
        return caminho, limite

    # BUSCA BIDIRECIONAL
    #def bidirecional(self, inicio, fim, nos, grafo):
    def bidirecional(self,inicio, fim, mapa,dim_x,dim_y ):
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
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)

        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)

        visitado2 = []
        linha = []
        linha.append(fim)
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

                #ind = nos.index(atual.estado)
                filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)
                # varre todos as conexões dentro do grafo a partir de atual
                #for novo in grafo[ind]:
                # for novo in filhos:
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

                #ind = nos.index(atual.estado)
                filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)

                # varre todos as conexões dentro do grafo a partir de atual
                #for novo in grafo[ind]:
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

        return "caminho não encontrado"
