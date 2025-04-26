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
raio = 20

# Coordenadas do objeto retângulo
base_ret = 30
altura_ret = 50

# Coordenadas do objeto triângulo
#base_tri = 80
#altura_tri = 100

x_enemy = randint(40, 600) # Posição aleatória do retângulo no eixo x
y_enemy = randint(40, 500) # Posição aleatória do retângulo no eixo y
'''
x_auxiliar = randint(50, 650) # Posição aleatória do triângulo no eixo x
y_auxiliar = randint(60, 550) # Posição aleatória do triângulo no eixo y

# Define os vértices do triângulo
vertices_triangulo = [
    (x_auxiliar, y_auxiliar), 
    (x_auxiliar + base_tri, y_auxiliar), 
    (x_auxiliar + base_tri / 2, y_auxiliar - altura_tri)
]
# Criação de um triângulo isósceles - 2 lados iguais
'''
branco = (255, 255, 255)
vermelho = (255, 0, 0)
dark_green = (0, 100, 0)
dark_blue = (0, 0, 100)
relogio = pygame.time.Clock()


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desenhando um Círculo")

running = True
while running:
    relogio.tick(60)  # 60 FPS
    tela.fill(dark_blue)
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
    enemy = pygame.draw.rect(tela, branco, (x_enemy, y_enemy, base_ret, altura_ret)) # desenha o retângulo
    #auxiliar = pygame.draw.polygon(tela, dark_blue, vertices_triangulo) # desenha o triângulo

    # colisão do enemy e do player
    if player.colliderect(enemy):
        x_enemy = randint(40, 600)
        y_enemy = randint(40, 500)
        print("Colidiu!")
    pygame.display.flip()  # Atualiza a tela
'''
    # colisão do auxiliar e do player
    if player.colliderect(auxiliar):
        x_auxiliar = randint(50, 650)
        y_auxiliar = randint(60, 550)
        vertices_triangulo = [
            (x_auxiliar, y_auxiliar), 
            (x_auxiliar + base_tri, y_auxiliar), 
            (x_auxiliar + base_tri / 2, y_auxiliar - altura_tri)
        ]
        print("Colidiu!")
    pygame.display.flip()  # Atualiza a tela
'''
pygame.quit()