# Rotina sucessores para Grade de Ocupação
def sucessores(atual,mapa):
    f = []

    x = atual[0]
    y = atual[1]

    if x+1 < len(mapa):
        if mapa[x+1][y]>0:
            linha = []
            linha.append(x+1)
            linha.append(y)
            f.append(linha)

    if x-1 >= 0:
        if mapa[x-1][y]>0:
            linha = []
            linha.append(x-1)
            linha.append(y)
            f.append(linha)

    if y+1 < len(mapa[0]):
        if mapa[x][y+1]>0:
            linha = []
            linha.append(x)
            linha.append(y+1)
            f.append(linha)

    if y-1 >= 0:
        if mapa[x][y-1]>0:
            linha = []
            linha.append(x)
            linha.append(y-1)
            f.append(linha)

    return f


def gerar_mapa(mapa):
    _mapa = []

    for linha in mapa.split('-'):
        _mapa.append([int(i) for i in linha.split(',')])

    return _mapa
