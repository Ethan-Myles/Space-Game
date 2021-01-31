import pygame

WHITE = (255, 255, 255)
GREEN = (0,255,0)

class Elementbox(pygame.sprite.Sprite):

    def __init__(self, surface5, color, width, height):
        super().__init__()

        self.image = surface5

        pygame.draw.rect(self.image, color, [0, 0, width, height])


        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels


