import pygame
pygame.init()

largura = 600
altura = 400

#coordenadas do objeto
centro_x = 300
centro_y = 200
raio = 50
color = pygame.Color('#0000FF')

tela = pygame.display.set_mode((largura, altura)) #configuração de largura e altura na tela

 #criando o objeto círculo
pygame.draw.circle(tela, color, (centro_x, centro_y), raio)
        
# Atualiza a tela
pygame.display.flip()        

# Espera até o usuário fechar a janela
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

