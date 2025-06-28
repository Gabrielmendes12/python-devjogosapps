import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Iniciar o pygame
pygame.init()

# Largura e altura da tela
largura = 640
altura = 480

# Inicialização da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha com Imagens e Fundo')


# --- Carregar Imagens ---
try:
    # Imagem para o Player (cabeça da cobra)
    imagem_player = pygame.image.load('imagens/capivaramer.png').convert_alpha()
    imagem_player = pygame.transform.scale(imagem_player, (100, 100))

    # Imagem para o Snack (comida)
    imagem_snack = pygame.image.load('imagens/coca.png').convert_alpha()
    imagem_snack = pygame.transform.scale(imagem_snack, (50, 50))


    # --- NOVA IMAGEM DE FUNDO ---
    # Carrega a imagem de fundo e a redimensiona para o tamanho da tela
    imagem_fundo = pygame.image.load('imagens/mar.jpg').convert() # Use .convert() se não tiver transparência
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

except pygame.error as e:
    print(f"Erro ao carregar uma das imagens: {e}")
    pygame.quit()
    exit()

# Som de fundo
pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('sons/bossa_nova.mp3')
pygame.mixer.music.play(-1)

# Som de colisão do inimigo
som_colisao = pygame.mixer.Sound('sons/laser1.wav')
som_colisao.set_volume(0.9)


# Posição do player (múltiplos de 20 para alinhar com o corpo)
x_player = (largura // 2) // 20 * 20
y_player = (altura // 2) // 20 * 20

# Velocidade da cobrinha (em múltiplos de 20 para movimentar em blocos)
velocidade = 10
# Direção inicial da cobrinha
x_controle = velocidade
y_controle = 0

# --- FUNÇÃO PARA GERAR POSIÇÃO DA COMIDA COM SEGURANÇA ---
def gerar_posicao_snack():
    margem_x = 20
    margem_y = 20

    num_colunas_disponiveis = (largura - 2 * margem_x) // 20
    num_linhas_disponiveis = (altura - 2 * margem_y) // 20

    if num_colunas_disponiveis <= 0 or num_linhas_disponiveis <= 0:
        print("Erro: A tela é muito pequena para gerar comida com as margens especificadas.")
        pygame.quit()
        exit()

    coluna_aleatoria = randint(0, num_colunas_disponiveis - 1)
    linha_aleatoria = randint(0, num_linhas_disponiveis - 1)

    x = margem_x + coluna_aleatoria * 20
    y = margem_y + linha_aleatoria * 20
    
    return x, y

# Posição inicial da comida
x_snack, y_snack = gerar_posicao_snack()


# Lista de cores (o fundo agora será a imagem)
cores = {
    "branco": (255, 255, 255),
    "preto": (0, 0, 0),
    "vermelho": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255), # Cor do corpo da cobra
    "amarelo": (255, 255, 0),
    "roxo": (128, 0, 128)
}

# Configuração da fonte
fonte = pygame.font.SysFont('Arial', 30, True, True)
# Variavel dos pontos
pontos = 0

# Relógio para controlar a taxa dos frames
relogio = pygame.time.Clock()

lista_corpo = []  # Lista para armazenar as posições do corpo da cobra
comprimento_inicial = 5 # Comprimento inicial da cobra
perdeu = False # Variável para controlar o estado de game over

# Função para Aumentar o Corpo da Cobra
def aumentar_corpo(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela, (cores["verde"]), (XeY[0], XeY[1], 30, 30))
       
# Função para Reiniciar o Jogo
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_player, y_player, x_snack, y_snack, lista_corpo, perdeu, x_controle, y_controle

    pontos = 0
    comprimento_inicial = 5
    x_player = (largura // 2) // 20 * 20
    y_player = (altura // 2) // 20 * 20
    x_controle = velocidade
    y_controle = 0
    lista_corpo = []
    x_snack, y_snack = gerar_posicao_snack()
    perdeu = False

# Loop Principal do Jogo
while True:
    relogio.tick(10)
    
    # --- DESENHA A IMAGEM DE FUNDO PRIMEIRO ---
    tela.blit(imagem_fundo, (0, 0)) # Desenha a imagem de fundo na posição (0,0)

    pontuacao = f'Pontos: {pontos}'
    renderizacao = fonte.render(pontuacao, True, (cores["branco"]))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a and x_controle != velocidade:
                x_controle = -velocidade
                y_controle = 0
            if event.key == K_d and x_controle != -velocidade:
                x_controle = velocidade
                y_controle = 0
            if event.key == K_s and y_controle != -velocidade:
                y_controle = velocidade
                x_controle = 0
            if event.key == K_w and y_controle != velocidade:
                y_controle = -velocidade
                x_controle = 0
            if event.key == K_SPACE and perdeu:
                reiniciar_jogo()

    if not perdeu:
        x_player += x_controle
        y_player += y_controle

        player_rect = imagem_player.get_rect(topleft=(x_player, y_player))
        snack_rect = imagem_snack.get_rect(topleft=(x_snack, y_snack))

        if player_rect.colliderect(snack_rect):
            x_snack, y_snack = gerar_posicao_snack()
            pontos += 1
            som_colisao.play()
            comprimento_inicial += 1

        lista_cabeca = [x_player, y_player]
        lista_corpo.append(lista_cabeca)

        for segmento in lista_corpo[:-1]:
            if segmento == lista_cabeca:
                perdeu = True
                break

        if x_player < 0 or x_player >= largura or y_player < 0 or y_player >= altura:
             perdeu = True

        if len(lista_corpo) > comprimento_inicial:
            del lista_corpo[0]

        aumentar_corpo(lista_corpo[:-1])

        tela.blit(imagem_player, player_rect)
        tela.blit(imagem_snack, snack_rect)

    if perdeu:
        fonte2 = pygame.font.SysFont('Arial', 20, True, True)
        mensagem = 'Game Over! Aperte a tecla Espaco para reiniciar'
        renderizacao2 = fonte2.render(mensagem, True, cores["vermelho"])
        posicaoTexto = renderizacao2.get_rect(center=(largura / 2, altura / 2))
        tela.blit(renderizacao2, posicaoTexto)

    tela.blit(renderizacao, (450, 40))
    pygame.display.update()