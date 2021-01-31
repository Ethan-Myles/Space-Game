from asteroids import Asteroid
from difficultmenu import game_difficulty
from elementbox import Elementbox
from intromenu import game_intro
from laser import Laser
from leaderboard import game_leaderboard
from overmenu import game_over
import pygame
from rocket import Rocket
from stars import Star
import random
from textbox import Textbox
import time

import inspect

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
GREY = (210,210,210)
DARKGREY = (88,88,88)
BLUE = (0, 191, 255)

WIDTH = 1000
HEIGHT= 650


score = 0
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Elements Game")

all_sprites_list = pygame.sprite.Group()

all_flying = pygame.sprite.Group()

# ----------------------------------------------------------------------------
# This group stores the instances of all asteroids. There are always three of
# them. It is global as it is referred to in the main while loop 'carryOn'.
# ----------------------------------------------------------------------------
all_asteroids = pygame.sprite.Group()

# === Create background stars ===
for i in range (1,40):
    surface2 = pygame.Surface([20,20],pygame.SRCALPHA)
    newstar = Star(surface2, WHITE, (10, 10), random.randint(1, 2), 20)  # surface, colour, position, radius, speed
    all_flying.add(newstar)
    all_sprites_list.add(newstar)

# === initalise font object to render text later ===
font = pygame.font.Font('OpenSans-Semibold.ttf', 24)

carryOn = True
clock = pygame.time.Clock()

# === Two menu screens before main game ===

selection = game_difficulty(screen,BLACK,WHITE,BLUE,font,WIDTH,HEIGHT,Star,clock)

username = game_intro(WIDTH,HEIGHT,screen,BLACK,WHITE,font,Star,clock)

print(selection)

# === Asteriod1 ===

surface3 = pygame.Surface([20,20],pygame.SRCALPHA)
asteroid1 = Asteroid(surface3, WHITE, (250,30), random.randint(1, 2), 2)  # surface, colour, position, radius, speed
asteroid1.rect.x = random.randint(1000,1500)
asteroid1.rect.y = random.randint(100,180)
asteroid1.speed = random.randint(100,400)/100
asteroid1.aSelection(selection)

all_flying.add(asteroid1)
all_asteroids.add(asteroid1)
all_sprites_list.add(asteroid1)


# === Asteroid2 ===

surface3 = pygame.Surface([20,20],pygame.SRCALPHA)
asteroid2 = Asteroid(surface3, WHITE, (3,30), random.randint(1, 2), 2)  # surface, colour, position, radius, speed
asteroid2.rect.x = random.randint(1000,1500)
asteroid2.rect.y = random.randint(220,310)
asteroid2.speed = random.randint(100,400)/100
asteroid2.aSelection(selection)

all_flying.add(asteroid2)
all_asteroids.add(asteroid2)
all_sprites_list.add(asteroid2)


# === Asteroid3 ===
surface3 = pygame.Surface([20,20],pygame.SRCALPHA)
asteroid3 = Asteroid(surface3, WHITE, (40,30), random.randint(1, 2), 2)  # surface, colour, position, radius, speed
asteroid3.rect.x = random.randint(1000,1500)
asteroid3.rect.y = random.randint(350,500)
asteroid3.speed = random.randint(100,400)/100
asteroid3.aSelection(selection)

all_flying.add(asteroid3)
all_asteroids.add(asteroid3)
all_sprites_list.add(asteroid3)

# === Create laser ===

surface4 = pygame.Surface([50,5],pygame.SRCALPHA)
newLaser = Laser(surface4,RED, 50, 5)

newLaser.rect.x = 400
newLaser.rect.y = -250
all_sprites_list.add(newLaser)

# === Create rocket ===
surface1 = pygame.Surface([WIDTH,HEIGHT])
playerRocket = Rocket(surface1, RED)
all_sprites_list.add(playerRocket)


# === Create the box that stores the question and the score ===
surface5 = pygame.Surface([400,100])
elementBox = Elementbox(surface5, DARKGREY, 400, 100)
all_sprites_list.add(elementBox)


# === read elements from file ===
file = open("Elements.txt", "r")
elementList = []
for line in file:
    data = line.split(",")
    elementName = data[0]  # doesn't store in a list only splits the data, needed to create a new list with the
    elementSymbol = data[1]
    elementSymbol = elementSymbol.strip('\n')
    elementList.append([elementName, elementSymbol])
correctElement  = (random.choice(elementList))
print(correctElement[0],correctElement[1])
incorrectElement1  = (random.choice(elementList))
incorrectElement2  = (random.choice(elementList))
answers = [correctElement,incorrectElement1,incorrectElement2]
random.shuffle(answers)
asteroid1.setElement(answers[0])
asteroid2.setElement(answers[1])
asteroid3.setElement(answers[2])

pygame.mixer.music.load('mainMusic.wav')
pygame.mixer.music.play(-1)

# === main loop ===
while carryOn:

    clock.tick(60)


    # === Deal with top-level events ===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    # === User input handling ===
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerRocket.moveUp(10)
    elif keys[pygame.K_s]:
        playerRocket.moveDown(10)
    if keys[pygame.K_SPACE]: # This is an if so you can hold spacebar and move.
        if newLaser.fired==False:
            effect = pygame.mixer.Sound('laser.wav')
            effect.set_volume(1)
            effect.play()
            newLaser.fire(playerRocket.rect.x, playerRocket.rect.y + playerRocket.height//2)

    # Creates boundaries by moving in the opposite direction, at the same speed so the rocket can't move past these points
    if playerRocket.rect.y == 105:
        playerRocket.moveDown(10)
    if playerRocket.rect.y == 555:
        playerRocket.moveUp(10)

    newLaser.move(70)

    #Detect if laser hits an asteroid
    if newLaser.fired:
        asteroid_collision_list = pygame.sprite.spritecollide(newLaser,all_asteroids,False)
        for asteroid in asteroid_collision_list:
                print("Asteroid Hit!")

                if asteroid.getSymbol()==correctElement[1]:
                    print("Correct answer")
                    score +=1
                    #Generate new question
                    correctElement = (random.choice(elementList))
                    print(correctElement[0],correctElement[1])
                    incorrectElement1  = (random.choice(elementList))
                    incorrectElement2  = (random.choice(elementList))
                    answers = [correctElement,incorrectElement1,incorrectElement2]
                    random.shuffle(answers)
                    asteroid1.setElement(answers[0])
                    asteroid2.setElement(answers[1])
                    asteroid3.setElement(answers[2])
                    asteroid1.rect.x = random.randint(1000,1500)
                    asteroid1.rect.y = random.randint(100,180)
                    asteroid2.rect.x = random.randint(1000,1500)
                    asteroid2.rect.y = random.randint(220,310)
                    asteroid3.rect.x = random.randint(1000,1500)
                    asteroid3.rect.y = random.randint(350,500)
                    asteroid1.changeSpeed()
                    asteroid2.changeSpeed()
                    asteroid3.changeSpeed()
                else:
                    asteroid1.changeSpeed()
                    asteroid2.changeSpeed()
                    asteroid3.changeSpeed()
                    print("Wrong answer")
                    score -=1

                newLaser.hide()
                #respawn asteroid
                asteroid.rect.x = random.randint(1000,1500)
                asteroid.rect.y = random.randint(100,180)

    # do this for rocket
    asteroid_collision_list = pygame.sprite.spritecollide(playerRocket,all_asteroids,False,pygame.sprite.collide_mask)
    for asteroid in asteroid_collision_list:
                print("Rocket Crash")
                pygame.mixer.music.stop()
                effect = pygame.mixer.Sound('gameover.wav')
                effect.play()

                game_over(font,WHITE,BLACK,WIDTH,HEIGHT,clock,screen,Star,username,score)

                #respawn asteroid
                asteroid.rect.x = random.randint(1000,1500)
                asteroid.rect.y = random.randint(100,180)
                score = 0

        # === Move all the stars and asteroids ===
    for moving_object in all_flying:
        if moving_object.moveLeft(): #moveLeft returns True if it had to respawn the asteroid to the right of the screen
            if moving_object.getSymbol() == correctElement[1]:
                correctElement = (random.choice(elementList))
                print(correctElement[0],correctElement[1])
                incorrectElement1  = (random.choice(elementList))
                incorrectElement2  = (random.choice(elementList))
                answers = [correctElement,incorrectElement1,incorrectElement2]
                random.shuffle(answers)
                asteroid1.setElement(answers[0])
                asteroid2.setElement(answers[1])
                asteroid3.setElement(answers[2])
                asteroid1.rect.x = random.randint(1000,1500)
                asteroid1.rect.y = random.randint(100,180)
                asteroid2.rect.x = random.randint(1000,1500)
                asteroid2.rect.y = random.randint(220,310)
                asteroid3.rect.x = random.randint(1000,1500)
                asteroid3.rect.y = random.randint(350,500)
            else:
                incorrectElement = (random.choice(elementList))
                moving_object.setElement(incorrectElement)



    # Updates the sprites on the screen
    all_sprites_list.update()

    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    if score > 0:
        colourChange = GREEN

    elif score < 0:
        colourChange = RED
    else:
        colourChange = WHITE

    # === Display element's name  ===
    question = font.render(correctElement[0], True, (WHITE))
    textWidth = question.get_width()
    screen.blit(question, ((200-textWidth)/2, 30))

    scoreText = font.render(str(score),True,(colourChange))
    screen.blit(scoreText, ((290), 30))
    scoreWord = font.render('Score:', True, (WHITE))
    screen.blit(scoreWord, ((200), 30))

    aWidth1 = asteroid1.image.get_width()
    aWidth2 = asteroid2.image.get_width()
    aWidth3 = asteroid3.image.get_width()


    pygame.display.flip()

pygame.quit()

