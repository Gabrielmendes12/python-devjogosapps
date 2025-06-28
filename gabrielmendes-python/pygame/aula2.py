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
altura_ret = 40

# Coordenadas do objeto triângulo
#base_tri = 80
#altura_tri = 100

x_enemy = randint(40, 600) # Posição aleatória do retângulo no eixo x
y_enemy = randint(40, 500) # Posição aleatória do retângulo no eixo y

# Cores
cores = {
'branco' : (255, 255, 255),
'vermelho' : (255, 0, 0),
'dark_green' : (0, 100, 0),
'dark_blue' : (0, 0, 100)
}
relogio = pygame.time.Clock()

lista_corpo = []
comprimento_inicial = 5

def aumentar_corpo(lista_corpo):
   for XeY in lista_corpo:
         pygame.draw.rect(tela, cores['dark_green'], (XeY[0], XeY[1], base_ret, altura_ret))

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desenhando um Círculo")

fonte = pygame.font.SysFont('times new roman', 28, True)
score = 0

# Carregar e tocar a música
pygame.mixer.music.load('sons/bossa_nova.mp3')
pygame.mixer.music.play(-1)  # -1 para tocar em loop

running = True
while running:
    relogio.tick(60)
    tela.fill(cores['dark_blue'])
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

        
    enemy = pygame.draw.circle(tela, cores['vermelho'], (x_enemy, y_enemy), raio) # desenha o círculo
    player = pygame.draw.rect(tela, cores['dark_green'], (centro_x, centro_y, base_ret, altura_ret)) # desenha o retângulo


    # colisão do enemy e do player
    if player.colliderect(enemy):
        x_enemy = randint(40, 600)
        y_enemy = randint(40, 500)
        score += 1
        som_colisao = pygame.mixer.Sound('sons/laser1.wav')
        som_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(centro_x)
    lista_cabeca.append(centro_y)
    lista_corpo.append(lista_cabeca)

    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]

    aumentar_corpo(lista_corpo)

    # renderização do texto
    texto_score = fonte.render(f"Pontuação: {score}", True, cores['branco'])
    tela.blit(texto_score,(300, 20))
    pygame.display.flip()  # Atualiza a tela


pygame.quit()