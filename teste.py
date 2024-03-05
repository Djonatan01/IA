import streamlit as st
import numpy as np

# Definindo as dimensões do grid
GRID_SIZE = 10

# Função para desenhar o grid do Pac-Man
def draw_grid(grid_size, pac_man_position):
    grid = np.zeros((grid_size, grid_size), dtype=int)
    grid[pac_man_position[0], pac_man_position[1]] = 1
    return grid

def main():
    st.title('Pac-Man Grid')

    # Posição inicial do Pac-Man
    pac_man_position = [0, 0]

    # Desenha o grid inicial
    grid = draw_grid(GRID_SIZE, pac_man_position)

    # Exibe o grid na interface
    st.write(grid)

    # Botões de movimento
    st.write("Controles do Pac-Man:")
    col1, col2, col3, col4 = st.columns(4)
    if col2.button('↑'):
        pac_man_position[0] = max(0, pac_man_position[0] - 1)
    if col1.button('←'):
        pac_man_position[1] = max(0, pac_man_position[1] - 1)
    if col3.button('→'):
        pac_man_position[1] = min(GRID_SIZE - 1, pac_man_position[1] + 1)
    if col4.button('↓'):
        pac_man_position[0] = min(GRID_SIZE - 1, pac_man_position[0] + 1)

    # Atualiza o grid após o movimento do Pac-Man
    grid = draw_grid(GRID_SIZE, pac_man_position)

    # Exibe o grid atualizado
    st.write(grid)

if __name__ == '__main__':
    main()
