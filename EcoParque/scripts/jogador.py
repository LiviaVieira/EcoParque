import pygame


class Jogador:

    def __init__(self):
        self.imagem = pygame.image.load(
            "assets/personagem_frente.png"
        )

        self.imagem = pygame.transform.scale(
            self.imagem, (50, 70)
        )

        self.x = 375
        self.y = 450

        self.velocidade = 5

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def atualizar(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade

        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidade

        if teclas[pygame.K_UP]:
            self.y -= self.velocidade

        if teclas[pygame.K_DOWN]:
            self.y += self.velocidade