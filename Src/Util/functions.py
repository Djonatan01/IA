def verificar_presenca(array, ponto):
    for coordenada in array:
        if coordenada == ponto:
            return True
    return False

# Rotina sucessores para Grade de Ocupação
def sucessores(atual, mapa, portal_map):
    f = []

    x = atual[0]
    y = atual[1]

    top = []
    left = []
    right = []
    bottom = []

    right.append(x+1)
    right.append(y)

    left.append(x-1)
    left.append(y)

    top.append(x)
    top.append(y+1)

    bottom.append(x)
    bottom.append(y-1)

    if verificar_presenca(portal_map, atual):

        if atual[0] == 0:
            top = []
            top.append(len(mapa)-1)
            top.append(y)
        elif atual[0] == len(mapa)-1:
            bottom = []
            bottom.append(0)
            bottom.append(y)

        if atual[1] == 0:
            left = []
            left.append(x)
            left.append(len(mapa[0])-1)
        elif atual[1] == len(mapa[0])-1:
            right = []
            right.append(x)
            right.append(0)


    if right[0] < len(mapa):
        if mapa[right[0]][right[1]] > 0:
            f.append(right)

    if left[0] >= 0:
        if mapa[left[0]][left[1]] > 0:
            f.append(left)

    if top[1] < len(mapa[0]):
        if mapa[top[0]][top[1]] > 0:
            f.append(top)

    if bottom[1] >= 0:
        if mapa[bottom[0]][bottom[1]] > 0:
            f.append(bottom)

    return f


def gerar_mapa(mapa):
    _mapa = []

    for linha in mapa.split('-'):
        _mapa.append([int(i) for i in linha.split(',')])

    return _mapa
