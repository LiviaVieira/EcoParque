import pygame
import sys

from scripts.jogador import Jogador
from scripts.lixo import Lixo
from scripts.lixeira import Lixeira

pygame.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("EcoParque")

relogio = pygame.time.Clock()

fonte = pygame.font.SysFont("arial", 24, bold=True)
fonte_mensagem = pygame.font.SysFont("arial", 20, bold=True)

VERDE = (46, 125, 50)
VERDE_CLARO = (232, 245, 233)
BRANCO = (255, 255, 255)
PRETO = (35, 50, 35)
VERMELHO = (198, 40, 40)

pontuacao = 0
lixo_carregado = None
mensagem = "Encontre um lixo para comecar!"
cor_mensagem = PRETO

cenario = pygame.image.load("assets/cenario_parque.png")
cenario = pygame.transform.scale(cenario, (LARGURA, ALTURA))

jogador = Jogador()

lixos = [
    Lixo("papel", 150, 150),
    Lixo("plastico", 300, 300),
    Lixo("metal", 550, 180),
    Lixo("vidro", 650, 400)
]

lixeiras = [
    Lixeira("papel", 300, 500),
    Lixeira("plastico", 365, 500),
    Lixeira("metal", 430, 500),
    Lixeira("vidro", 495, 500)
]

rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE:

                jogador_rect = pygame.Rect(
                    jogador.x,
                    jogador.y,
                    50,
                    70
                )

                if lixo_carregado is None:

                    for lixo in lixos:

                        if jogador_rect.colliderect(lixo.get_rect()):
                            lixo.coletado = True
                            lixo_carregado = lixo
                            mensagem = "Leve o lixo ate a lixeira!"
                            cor_mensagem = PRETO
                            break

                else:

                    for lixeira in lixeiras:

                        if jogador_rect.colliderect(lixeira.get_rect()):

                            if lixo_carregado.tipo == lixeira.tipo:
                                pontuacao += 10
                                lixos.remove(lixo_carregado)
                                lixo_carregado = None
                                mensagem = "Muito bem! +10 pontos!"
                                cor_mensagem = VERDE

                            else:
                                mensagem = "Lixeira incorreta! Tente outra."
                                cor_mensagem = VERMELHO

                            break

    tela.blit(cenario, (0, 0))

    jogador.atualizar()
    jogador.desenhar(tela, lixo_carregado)

    for lixo in lixos:
        lixo.desenhar(tela)

    for lixeira in lixeiras:
        lixeira.desenhar(tela)

    painel_pontos = pygame.Rect(15, 15, 220, 65)

    pygame.draw.rect(
        tela,
        BRANCO,
        painel_pontos,
        border_radius=15
    )

    pygame.draw.rect(
        tela,
        VERDE,
        painel_pontos,
        3,
        border_radius=15
    )

    texto_pontos = fonte.render(
        f"PONTOS: {pontuacao}",
        True,
        VERDE
    )

    tela.blit(texto_pontos, (30, 34))

    painel_mensagem = pygame.Rect(15, 90, 400, 42)

    pygame.draw.rect(
        tela,
        VERDE_CLARO,
        painel_mensagem,
        border_radius=12
    )

    texto_mensagem = fonte_mensagem.render(
        mensagem,
        True,
        cor_mensagem
    )

    tela.blit(texto_mensagem, (25, 101))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()