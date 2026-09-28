import pygame
import sys

from scripts.jogador import Jogador

pygame.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("EcoParque")

relogio = pygame.time.Clock()

cenario = pygame.image.load("assets/cenario_parque.png")
cenario = pygame.transform.scale(cenario, (LARGURA, ALTURA))

jogador = Jogador()

rodando = True

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(cenario, (0, 0))

    jogador.atualizar()
    jogador.desenhar(tela)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()