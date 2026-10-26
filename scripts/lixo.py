import pygame


class Lixo:

    def __init__(self, tipo, x, y):
        self.tipo = tipo
        self.x = x
        self.y = y

        imagens = {
            "papel": "assets/lixo_papel.png",
            "plastico": "assets/lixo_plastico.png",
            "metal": "assets/lixo_metal.png",
            "vidro": "assets/lixo_vidro.png"
        }

        self.imagem = pygame.image.load(imagens[tipo])
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))

        self.coletado = False

    def desenhar(self, tela):
        if not self.coletado:
            tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 50, 50)