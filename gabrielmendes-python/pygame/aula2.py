import pygame
from pygame.locals import*
from random import randint

pygame.init()

# medidas da tela 
largura = 800
altura = 600

# Coordenadas do objeto círculo
centro_x = largura / 2  # Centraliza o círculo na tela
centro_y = altura / 2  # Centraliza o círculo na tela
raio = 50

# Coordenadas do objeto retângulo
base_ret = 80
altura_ret = 100

x_enemy = randint(40, 600) # Posição aleatória do retângulo no eixo x
y_enemy = randint(40, 500) # Posição aleatória do retângulo no eixo y

branco = (255, 255, 255)
vermelho = (255, 0, 0)
dark_green = (0, 100, 0)
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desenhando um Círculo")

running = True
while running:
    relogio.tick(60)  # 60 FPS
    tela.fill(branco)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.key.get_pressed()[K_a]:
            centro_x = centro_x - 10 # Move o círculo para a esquerda
        if pygame.key.get_pressed()[K_d]:
            centro_x = centro_x + 10 # Move o círculo para a direita
        if pygame.key.get_pressed()[K_w]:
            centro_y = centro_y - 10 # Move o círculo para cima
        if pygame.key.get_pressed()[K_s]:
            centro_y = centro_y + 10 # Move o círculo para baixo
        
    player = pygame.draw.circle(tela, vermelho, (centro_x, centro_y), raio) # desenha o círculo
    enemy = pygame.draw.rect(tela, dark_green, (x_enemy, y_enemy, base_ret, altura_ret)) # desenha o retângulo

    # colisão do enemy e do player
    if player.colliderect(enemy):
        x_enemy = randint(40, 600)
        y_enemy = randint(40, 500)
        print("Colidiu!")
    pygame.display.flip()  # Atualiza a tela

pygame.quit()