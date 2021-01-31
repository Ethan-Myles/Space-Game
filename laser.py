import pygame
import random
RED = (255,0,0)
WHITE = (255, 255, 255)

class Laser(pygame.sprite.Sprite):

    def __init__(self,surface4, color, width, height):
        super().__init__()

        self.image = surface4

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
        self.fired = False


    def moveUp(self, pixels):
        if not self.fired:
            self.rect.y -= pixels

    def moveDown(self, pixels):
        if not self.fired:
            self.rect.y += pixels

    def fire(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.fired = True

    def move(self, pixels):
        if self.fired:
            self.rect.x += pixels
            if self.rect.x > 1000:
                self.rect.x = 400
                self.rect.y = -250
                self.fired = False


    def hide(self):
        self.fired = False
        self.rect.x = -500 #off screen
