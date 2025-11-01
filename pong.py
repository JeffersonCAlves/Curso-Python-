# baixar o Pygame e Importar o Pygame
import pygame

# iniciar o Pygame
pygame.init()


# variaveis relevante para o jogo

# cores
altura_tela = 600
largura_tela = 800

# Pontuacao

fonte_pontos = pygame.font.Font(None, 90)
pontos1 = 0
pontos2 = 0

# raquete

largura_raquete = 15
altura_raquete = 100

# classes / molde (reutilizar codigos) = blocos de codigos
# metodos: acoes que realiza
# funcao: o que vai acontecer quando eu criar uma raquete:

class Raquete: 
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, largura_raquete, altura_raquete)

    def desenhar(self, tela):
        pygame.draw.rect(tela, branco, self.rect)

    def mover(self, tecla_cima, tecla_baixo):

        teclas = pygame.key.get_pressed()

        # para subir:
        if teclas[tecla_cima] and self.rect.top > 0: # aqui defini o limite de acao da raquete
            self.rect.y -= 8 # aqui define a velocidade da raquete


        # para descer:
        if teclas[tecla_baixo]and self.rect.bottom < 600: # aqui defini o limite de acao da raquete
            self.rect.y += 8 # aqui define a velocidade da raquete
            

raquete1 = Raquete(10, 300)
raquete2 = Raquete(780, 300)


# Criar a bola do jogo

raio_bola = 10
velocidade_bola_x = 5
velocidade_bola_Y = 5

class Bola: 
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - raio_bola, y - raio_bola, raio_bola * 2, raio_bola * 2) # diametro da bola tamanho

        self.vel_x = velocidade_bola_x # bola comeca andando fixo aqui ela vai sempre para direita
        self.vel_Y = velocidade_bola_Y

    def desenhar(self, tela):
        pygame.draw.ellipse(tela, branco, self.rect)

    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_Y
    
    def verificar_colisao(self, raquete1, raquete2):
        # verificar se a bola bateu na parede
        if self.rect.top <= 0 or self.rect.bottom >= altura_tela:
            self.vel_Y *= -1

        # verificar se a bola bateu na raquete
        if self.rect.colliderect(raquete1) or self.rect.colliderect(raquete2):
            self.vel_x *= -1 # Inverte a direção X

        # bola voltar para o meio da tela apos pontuar
    def resetar(self):
        self.rect.x = largura_tela / 2 - raio_bola
        self.rect.y = altura_tela /2 - raio_bola

        # Extra inverter a velocidade da bola quando marcar ponto / um respiro no jogo
        pygame.time.delay(500) # Pausa por 0.5 seg


bola = Bola(400, 300)

# relogio
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('pong')

# cores:  criar as cores e formas geometricas do jogo
preto = (0, 0, 0)
branco = (255, 255, 255)


# iniciar o fluxo do jogo


# fluxo do jogo rodando

rodando = True

while rodando:
    # eventos que ocorrem no jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


    tela.fill(preto)

    raquete1.desenhar(tela)
    raquete1.mover(pygame.K_w, pygame.K_s)
    bola.desenhar(tela)

    raquete2.desenhar(tela)
    raquete2.mover(pygame.K_UP, pygame.K_DOWN)

    bola.mover()

    bola.verificar_colisao(raquete1.rect, raquete2.rect)

    if bola.rect.left < 0:
            pontos2 += 1
            bola.resetar()

    if bola.rect.right > largura_tela:
            pontos1 += 1
            bola.resetar()

    pygame.display.flip() # a partir daqui tudo que aparece na tela

    relogio.tick(60) # tempo de fraimes por segundos

pygame.quit()








