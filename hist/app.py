import streamlit as st
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
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
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
                st.table(matriz)
            else:
                matriz [xa][ya] = 10
