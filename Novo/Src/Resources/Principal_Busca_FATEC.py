import Util.functions as fa
import Src.Resources.Bidirecional as bs
from sys import exit

sol = bs.busca()
caminho = []

# Busca em Grade de Ocupação
mapa = fa.Gera_Problema_Grade("mapa.txt")
dim_x = len(mapa)
dim_y = len(mapa[0])

origem  = [0,0]
destino = [9,8]
print(mapa)
print(dim_x,dim_y)

if origem[0]<0  or origem[0]>dim_x-1  or origem[1]<0  or origem[1]>dim_y-1  or destino[0]<0 or destino[0]>dim_x-1 or origem[1]<0  or origem[1]>dim_y-1:
       print("Coordenada Inválida")
       exit()

caminho = sol.amplitude(origem,destino,mapa,dim_x,dim_y)
print("\n===> AMPLITUDE:",caminho)
print("===> Custo do Caminho:",len(caminho)-1)

caminho = sol.profundidade(origem,destino,mapa,dim_x,dim_y)
print("\n*****PROFUNDIDADE*****\n",caminho)
print("===> Custo do Caminho:",len(caminho)-1)

limeteTotal = dim_x * dim_y
limite = 1
while limite != -1:

    caminho = sol.prof_limitada(origem,destino,mapa,dim_x,dim_y,limite)
    print("\n***** PROFUNDIDADE LIMITADA ( L =",limite,")*****\n",caminho)
    if caminho[0]!="caminho não encontrado":
        print("===> Custo do Caminho:",len(caminho)-1)
        break
    else:
        if limite <= limeteTotal:
            if limite > limeteTotal:
                limite = limeteTotal
            else:
                limite += 10
        else:
            limite = -1

caminho = sol.bidirecional(origem,destino,mapa,dim_x,dim_y)
print("\n*****BIDIRECIONAL*****\n",caminho)
print("===> Custo do Caminho:",len(caminho)-1)