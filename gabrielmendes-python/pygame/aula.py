import pygame
pygame.init()

largura = 800
altura = 600

# Coordenadas do objeto círculo
centro_x = 0
centro_y = 0
raio = 0

# Coordenadas do objeto retângulo
pos_x = 650
pos_y = 50
base_ret = 100
altura_ret = 100

tela = pygame.display.set_mode((largura, altura))  # Configuração de largura e altura na tela

# Espera até o usuário fechar a janela
running = True
while running:
    # Preenche o fundo com a cor branca a cada iteração
    tela.fill((255, 255, 255))

    # Verifica os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza a posição do círculo
    centro_y += 1  # Movendo o círculo para baixo

    # Criando o objeto círculo azul 
    pygame.draw.circle(tela, (0, 0, 255), (centro_x, centro_y), raio)

    # Criando o objeto retângulo verde
    pygame.draw.rect(tela, (0, 255, 0), (pos_x, pos_y, base_ret, altura_ret))

    # Desenho da linha vermelha
    pygame.draw.line(tela, (255, 0, 0), (390, 0), (390, 600), 5)

    '''#Círculo está em loop -> vai e volta na tela
    if centro_y >= altura:
        centro_y = 0
    centro_y = centro_y+1'''

    if raio >= largura:
        raio = 0
    raio +=1


    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de atualização (FPS)
    pygame.time.Clock().tick(200)  # 60 FPS

pygame.quit()