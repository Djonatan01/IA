
import numpy as np

# Solicita ao usuário os valores de n e m
n = 10
m = 10
x = 0 # Exemplo de valor para x
y = 0 # Exemplo de valor para y
xa = 0 # Exemplo de valor para x
ya = 0 # Exemplo de valor para y

atual = [xa, ya]

matriz = [
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 1]

]

while True:
    for ya, row in enumerate(matriz):
        for xa, value in enumerate(row):
            print(f"x: {xa}, y: {ya}, value: {value}")
            if value == 1:
                # Exibe a matriz
                if matriz [ya][xa +1 ] == 1:
                    matriz [ya][xa] = 5
                elif matriz [ya+1][xa] == 1:
                    matriz [ya][xa] = 5
                    matriz [ya+1][xa] = 5
                elif matriz [ya][xa - 1] == 1 & xa > 0:
                    matriz [ya][xa - 1] = 5
            else:
                matriz [ya][xa] = 10