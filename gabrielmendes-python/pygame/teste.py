import pygame
from pygame.locals import *
from random import randint
from math import hypot

pygame.init()

# medidas da tela 
largura = 800
altura = 600

# Tamanho do corpo
base_ret = 30
altura_ret = 40

# Posição inicial do jogador
x = largura // 2
y = altura // 2

# Corpo do jogador (lista de segmentos)
corpo_jogador = [(x, y)]

# Inimigo (círculo)
raio = 20
x_enemy = randint(40, 760)
y_enemy = randint(40, 560)

# Cores
cores = {
    'branco': (255, 255, 255),
    'vermelho': (255, 0, 0),
    'dark_green': (0, 100, 0),
    'dark_blue': (0, 0, 100)
}

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo Estilo Cobrinha")

fonte = pygame.font.SysFont('times new roman', 28, True)
relogio = pygame.time.Clock()
score = 0

vel = 10  # Velocidade de movimento
direcao = 'RIGHT'

running = True
while running:
    relogio.tick(15)  # FPS

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_w] and direcao != 'DOWN':
        direcao = 'UP'
    if keys[K_s] and direcao != 'UP':
        direcao = 'DOWN'
    if keys[K_a] and direcao != 'RIGHT':
        direcao = 'LEFT'
    if keys[K_d] and direcao != 'LEFT':
        direcao = 'RIGHT'

    # Atualiza a posição do jogador
    x_ant, y_ant = corpo_jogador[0]
    if direcao == 'UP':
        y_ant -= vel
    elif direcao == 'DOWN':
        y_ant += vel
    elif direcao == 'LEFT':
        x_ant -= vel
    elif direcao == 'RIGHT':
        x_ant += vel

    # Insere nova posição na frente do corpo
    corpo_jogador.insert(0, (x_ant, y_ant))

    # Verifica colisão com círculo (usando distância)
    dist = hypot(x_ant + base_ret/2 - x_enemy, y_ant + altura_ret/2 - y_enemy)
    if dist < raio + base_ret / 2:
        score += 1
        x_enemy = randint(40, 760)
        y_enemy = randint(40, 560)
        # som_colisao = pygame.mixer.Sound('pygame/sons/laser1.wav')
        # som_colisao.play()
    else:
        corpo_jogador.pop()  # Remove o último segmento se não colidiu

    # Desenha tudo
    tela.fill(cores['dark_blue'])

    # Desenha o círculo (inimigo)
    pygame.draw.circle(tela, cores['vermelho'], (x_enemy, y_enemy), raio)

    # Desenha o corpo do jogador
    for segmento in corpo_jogador:
        pygame.draw.rect(tela, cores['dark_green'], (*segmento, base_ret, altura_ret))

    # Texto de pontuação
    texto_score = fonte.render(f"Pontuação: {score}", True, cores['branco'])
    tela.blit(texto_score, (300, 20))
    pygame.display.flip()

pygame.quit()
