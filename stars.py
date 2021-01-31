import pygame
import random

WHITE = (255, 255, 255)
GREEN = (34,139,34)
WIDTH=1000

class Star(pygame.sprite.Sprite):

    def __init__(self, surface2, color, pos, radius, speed):
        super().__init__()

        self.image = surface2
        self.radius = radius
        self.color = color
        self.speed = speed
        self.pos = pos

        pygame.draw.circle(self.image, self.color, self.pos, self.radius, 0)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1,1000)
        self.rect.y = random.randint(1,650)
    # This function is called to move the stars left. It is usually called by the main program loop.

    def moveLeft(self):

        self.rect.x -= self.speed/ 20

        # --- When the star hits the left of screen send it back to the right ---
        if self.rect.x < 0:
            self.changeSpeed(random.randint(50, 100))
            self.rect.x = WIDTH
            #print(SCREENWIDTH)

    def moveRight(self, pixels):
        self.rect.x += self.speed/20


    def changeSpeed(self, speed):
        self.speed = speed
