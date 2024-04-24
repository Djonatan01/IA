from Src.Models.ListaDEnc import lista_od
from Src.Util.functions import sucessores, weight


class CustoUniforme:
    def __init__(self, inicio, fim, mapa, portalMap, weightMap):
        self.inicio = inicio
        self.fim = fim
        self.mapa = mapa
        self.portalMap = portalMap
        self.weightMap = weightMap

    def make(self, inicio, fim):  
        l1 = lista_od()
        l2 = lista_od()
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

                return caminho[::-1]
            
            filhos = sucessores(atual.estado, self.mapa, self.portalMap)

            for novo in filhos:
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL

                v2 = atual.valor2 + weight(novo, self.weightMap)   # custo do caminho
                v1 = v2 # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.insereUltimo(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "error"    