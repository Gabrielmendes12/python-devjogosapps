import pygame
from pygame.locals import*
from random import randint

pygame.init()

# medidas da tela 
largura = 800
altura = 600

# Coordenadas do objeto círculo
x_player = largura / 2  # Centraliza o círculo na tela
y_player = altura / 2  # Centraliza o círculo na tela
raio = 20

#velocidade da cobrinha
vel = 5
#direção da cobrinha
x_controle = vel
y_controle = 0

# Coordenadas do objeto retângulo
base_ret = 30
altura_ret = 50

x_enemy = randint(40, 600) # Posição aleatória do retângulo no eixo x
y_enemy = randint(40, 500) # Posição aleatória do retângulo no eixo y


cores = {
    "branco": (255, 255, 255),
    "vermelho": (255, 0, 0),
    "dark_green": (0, 100, 0),
    "dark_blue": (0, 0, 100),
}
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Iniciando o jogo da cobrinha")
relogio = pygame.time.Clock()
lista_corpo = [] # lista para armazenar as posições do corpo da cobrinha
comprimento_inicial = 5
perdeu = False

#Função para desenhar o corpo da cobrinha
def aumentar_corpo(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela, cores["dark_green"], (XeY[0], XeY[1], base_ret, altura_ret))

#Função para reiniciar o jogo:
def reiniciar_jogo():
    global score, perdeu, x_player, y_player, x_enemy, y_enemy, comprimento_inicial, lista_corpo, lista_cabeca, perdeu
    
    score = 0
    x_player = largura / 2
    y_player = altura / 2
    comprimento_inicial = 5
    lista_corpo = []
    lista_cabeca = []
    x_enemy = randint(40, 600)
    y_enemy = randint(40, 500)
    perdeu = False


fonte = pygame.font.SysFont('times new roman', 28, True)
score = 0

# Carregar e tocar a música
pygame.mixer.music.set_volume(0.5)  # Define o volume da música (0.0 a 1.0)
pygame.mixer.music.load('pygame/sons/bossa_nova.mp3')
pygame.mixer.music.play(-1)  # -1 para tocar em loop

# Loop principal do jogo
while True:
    relogio.tick(30)  # 30 FPS
    tela.fill(cores["dark_blue"])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == vel:
                    pass
                else:
                    x_controle = -vel
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -vel:
                    pass
                else:
                    x_controle = vel
                    y_controle = 0

            if event.key == K_s:
                if y_controle == -vel:
                    pass
                else:
                    x_controle = 0
                    y_controle = vel
            if event.key == K_w:
                if y_controle == vel:
                    pass
                else:
                    x_controle = 0
                    y_controle = -vel        
    # Movimento do jogador
    x_player += x_controle
    y_player += y_controle
    # Criação dos objetos do jogo
    enemy = pygame.draw.circle(tela, cores["vermelho"], (x_enemy, y_enemy), raio) # desenha o círculo
    player = pygame.draw.rect(tela, cores["dark_green"], (x_player, y_player, base_ret, altura_ret)) # desenha o retângulo

    # colisão do enemy e do player
    if player.colliderect(enemy):
        x_enemy = randint(40, 600)
        y_enemy = randint(40, 500)
        score += 1
        som_colisao = pygame.mixer.Sound('pygame/sons/laser1.wav')
        som_colisao.play()
        comprimento_inicial += 1

    lista_cabeca = []
    lista_cabeca.append(x_player)
    lista_cabeca.append(y_player)
    lista_corpo.append(lista_cabeca) # adiciona a posição da cabeça na lista

    # renderização do texto
    texto_score = fonte.render(f"Pontuação: {score}", True, cores["branco"])
    tela.blit(texto_score,(300, 20))
    pygame.display.flip()  # Atualiza a tela
