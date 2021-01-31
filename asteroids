import pygame
import random

BlUE = (175,238,238)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
WIDTH = 1000


class Asteroid(pygame.sprite.Sprite):

    def __init__(self, surface3, color, pos, radius, speed):
        super().__init__()

        self.image = surface3
        self.radius = radius
        self.color = color
        self.speed = speed
        self.pos = pos
        self.__symbol = ""  #Private property
        self.__answer = ""  #Private property

        self.image = pygame.image.load("Asteroid.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image,random.randint(2,280))
        self.font = pygame.font.SysFont('OpenSans-Semibold.ttf', 30)
        self.textSurface = self.font.render(self.__symbol, 1, BlUE)
        W = self.textSurface.get_width()
        H = self.textSurface.get_height()
        self.image.blit(self.textSurface, [self.image.get_width()/2 - W/2, self.image.get_height()/2 - H/2])

        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 250

        #Create a mask for collision detection (with laser or rocket) to ignore transparent pixels
        self.mask = pygame.mask.from_surface(self.image)

    def aSelection(self, selection):
        if selection == 'Easy' :
            self.speed = 1.5
        elif selection == 'Medium' :
            self.speed = 3
        else:
            self.speed = 5
        print(str(self.speed) + " from aSelection")






    #=== input -  output - returns true if argument is, else returns false ===
    def moveLeft(self):
        self.rect.x -= self.speed
        if self.rect.x < -150:
            self.changeSpeed()
            self.rect.x = WIDTH
            return True
        return False



    def moveRight(self):
        self.rect.x += self.speed


    def changeSpeed(self):
        self.speed = self.speed + random.uniform(1,1.4) #.uniform is used to find a random float between the specificed range
        print(str(self.speed) + " from changeSpeed")
        if self.speed >= 9:
            self.speed = 9

    def setElement(self, element):  #A setter for the private properies symbol (e.g. Ti) and answer (e.g. Titane)
        self.__symbol = element[1]
        self.__answer = element[0]
        self.image = pygame.image.load("Asteroid.png").convert_alpha()
        self.textSurface = self.font.render(self.__symbol, 1, WHITE)
        W = self.textSurface.get_width()
        H = self.textSurface.get_height()
        self.image.blit(self.textSurface, [self.image.get_width()/2 - W/2, self.image.get_height()/2 - H/2])


    def getSymbol(self):  #A getter for the private properies symbol (e.g. Ti)
        return self.__symbol

    def getAnswer(self):  #A getter for the private properies answer (e.g. Titane)
        return self.__answer


