import numpy as np
import random as rd
import math

def verificar_presenca(array, ponto):
    for coordenada in array:
        if coordenada == ponto:
            return True
    return False

def weight(atual, weightMap):
    for weight in weightMap:
        if weight[0] == atual[0] and weight[1] == atual[1]:
            return weight[2] + 1

    return 0

def posicoes_possiveis(mapa):
    positions = []

    for x in range(len(mapa)):
        for y in range(len(mapa[0])):
            if(mapa[x][y] > 0):
                positions.append([x,y])

    return positions

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

def gera_H(ambient):
    n = len(ambient)

    h = np.zeros((n,n),int)

    i = 0

    for no_origem in ambient:
        j = 0
        ori_x, ori_y = no_origem
        for no_destino in ambient:
            if no_origem != no_destino:
                des_x, des_y = no_destino
                
                v  = round(math.sqrt((int(ori_x) - int(des_x))**2 + (int(ori_y) - int(des_y))**2) * 2, 0)

                h[i][j] = v*rd.uniform(0,1)
            j += 1
        i += 1
    
    return h
