import pygame
import sys
import Principal_Busca_FATEC as pr

# Inicializa o Pygame
pygame.init()

# Definindo constantes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
MOVE_SPEED = 1  # Velocidade de movimento
CELL_SIZE = 15  # Tamanho de cada célula na tela

# Definindo a classe do Pac-Man
class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Carrega a imagem do Pac-Man
        self.image = pygame.image.load("pacman.png").convert_alpha()  # Substitua "pacman.png" pelo caminho da sua imagem
        self.image = pygame.transform.scale(self.image, (30, 30))  # Redimensiona a imagem para 50x50
        self.rect = self.image.get_rect()
        self.rect.center = (50,50)
        self.move_queue = []  # Fila de movimentos a serem executados

    def update(self):
        if self.move_queue:
            move = self.move_queue.pop(0)
            self.rect.x += (move[0] * CELL_SIZE) * MOVE_SPEED
            self.rect.y += (move[1] * CELL_SIZE) * MOVE_SPEED


# Configuração da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Criando os sprites
all_sprites = pygame.sprite.Group()
pacman = Pacman()
all_sprites.add(pacman)

# Movimentos a serem executados (substitua esta lista pelos movimentos retornados pela busca em amplitude)
#movement_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
movement_list = pr.principal()

# Adiciona os movimentos à fila de movimentos do Pac-Man
pacman.move_queue.extend(movement_list)

# Loop principal do jogo
running = True
while running:
    # Verifica eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza
    all_sprites.update()
    # Desenha na tela
    screen.fill(BLACK)  # Altera a cor de fundo para preto
    all_sprites.draw(screen)
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
sys.exit()
