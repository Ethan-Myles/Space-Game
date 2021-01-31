import pygame
import random
from textbox import Textbox
import sys

def game_leaderboard(font,WHITE,BLACK,WIDTH,HEIGHT,clock,screen,Star,username,score,leaderboardTuple,numLines):
    lea = True

    while lea:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    # I need this to close the entire game and not just the Pygame library
                    sys.exit()

        screen.fill(BLACK)

        overText = font.render('Leaderboard', True, (WHITE))
        overtextW = overText.get_width()
        screen.blit(overText,((WIDTH-overtextW)/2,185))

        # for loop used to cycle through the different element pairs
        # changeY is used to increment the blitted username,score array pair on the leaderboard screen
        # numLines defined in overmenu.py explained use there

        changeY = 0
        for x in range(0,numLines):
            changeY += 30
            if x == 0:
                goldText = (str(leaderboardTuple[0][0]) + " " + str(leaderboardTuple[0][1]))
                leaderboardText = font.render(str(goldText), 1, (218,165,32))
                leaderboardtextW = leaderboardText.get_width()
                screen.blit(leaderboardText, ((WIDTH - leaderboardtextW) / 2, 200 + changeY))
            elif x == 1:
                silverText = (str(leaderboardTuple[1][0]) + " " + str(leaderboardTuple[1][1]))
                leaderboardText = font.render(str(silverText), 1, (192,192,192))
                leaderboardtextW = leaderboardText.get_width()
                screen.blit(leaderboardText, ((WIDTH - leaderboardtextW) / 2, 200 + changeY))
            elif x == 2:
                bronzeText = (str(leaderboardTuple[2][0]) + " " + str(leaderboardTuple[2][1]))
                leaderboardText = font.render(str(bronzeText), 1, (205,127,50))
                leaderboardtextW = leaderboardText.get_width()
                screen.blit(leaderboardText, ((WIDTH - leaderboardtextW) / 2, 200 + changeY))
            else:
                otherText = (str(leaderboardTuple[x][0]) + " " + str(leaderboardTuple[x][1]))
                leaderboardText = font.render(str(otherText), 1, (255, 255, 255))
                leaderboardtextW = leaderboardText.get_width()
                screen.blit(leaderboardText, ((WIDTH - leaderboardtextW) /2, 200 + changeY))

        for i in range (1,20):
            newStarx = random.randint(1, WIDTH)
            newStary = random.randint(1, HEIGHT)
            newstarDifficult = Star(screen, WHITE, (newStarx, newStary), random.randint(1, 2), 20)

        pygame.display.update()
        clock.tick(15)
