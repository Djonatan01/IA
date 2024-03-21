# Rotina sucessores para Grade de Ocupação
def sucessores(atual,mapa,dim_x,dim_y):
    f = []
    x = atual[0]
    y = atual[1]

    if y + 1 != dim_y:
        if mapa[x][y+1]==1:
            linha = []
            linha.append(x)
            linha.append(y+1)
            f.append(linha)
                            
    if x + 1 != dim_x:
        if mapa[x+1][y]==1:
            linha = []
            linha.append(x+1)
            linha.append(y)
            f.append(linha)
    
    if x - 1 >= 0:
        if mapa[x-1][y]==1:
            linha = []
            linha.append(x-1)
            linha.append(y)
            f.append(linha)
    
    if y - 1 >= 0:
        if mapa[x][y-1]==1:
            linha = []
            linha.append(x)
            linha.append(y-1)
            f.append(linha)
    
    return f

def Gera_Problema_Grade(arquivo):
    f = open(arquivo,"r")
    
    mapa = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        for i in range(len(str1)):
            str1[i] = int(str1[i])
        mapa.append(str1)
    
    return mapa