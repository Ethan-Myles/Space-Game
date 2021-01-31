import pygame

WHITE = (255, 255, 255)
GREEN = (0,255,0)

class Rocket(pygame.sprite.Sprite):

    def __init__(self, surface1, color):
        super().__init__()

        self.image = surface1
        self.image = pygame.image.load("RocketF.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 205
        self.width = 233
        self.height = 96


    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels
