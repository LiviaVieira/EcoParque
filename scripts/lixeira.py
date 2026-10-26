import pygame


class Lixeira:

    def __init__(self, tipo, x, y):
        self.tipo = tipo
        self.x = x
        self.y = y

        # Usamos os seus arquivos originais que têm o formato correto
        imagens = {
            "papel": "assets/lixeira_vermelha.png",   # Usamos a vermelha como molde perfeito para a azul
            "plastico": "assets/lixeira_vermelha.png", 
            "metal": "assets/lixeira_amarela.png",    
            "vidro": "assets/lixeira_verde.png"       
        }

        # Carrega a imagem e garante que podemos modificar seus pixels
        self.imagem = pygame.image.load(imagens[tipo]).convert_alpha()

        # Se for a lixeira de PAPEL, vamos trocar a paleta de cores (Vermelho -> Azul)
        if tipo == "papel":
            # Cria uma cópia para não alterar o arquivo original na memória
            self.imagem = self.imagem.copy()
            pixels = pygame.PixelArray(self.imagem)
            
            # Varre a imagem pixel por pixel substituindo os tons de vermelho por azul
            for x_pixel in range(self.imagem.get_width()):
                for y_pixel in range(self.imagem.get_height()):
                    cor = self.imagem.unmap_rgb(pixels[x_pixel, y_pixel])
                    
                    # Se o pixel tiver mais vermelho (R) do que verde (G) e azul (B), e não for branco/transparente
                    if cor.r > cor.g and cor.r > cor.b and cor.a > 0:
                        # Mantém a mesma intensidade de brilho que o vermelho tinha, mas aplica no canal azul!
                        pixels[x_pixel, y_pixel] = (0, int(cor.r * 0.4), cor.r, cor.a)
            
            # Fecha o array de pixels para liberar a imagem para o Pygame
            del pixels

        # Redimensiona todas para o tamanho padrão idêntico
        self.imagem = pygame.transform.scale(self.imagem, (70, 80))

        self.largura = 70
        self.altura = 80

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
