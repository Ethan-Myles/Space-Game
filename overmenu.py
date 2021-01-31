import pygame
import random
from leaderboard import game_leaderboard
from textbox import Textbox

def game_over(font,WHITE,BLACK,WIDTH,HEIGHT,clock,screen,Star,username,score):
    ove = True

    textObject = Textbox((WIDTH-200)/2, 340, 200, 24, 24, 20, True,"",(0, 191, 255),(255,255,255),(0, 191, 255))

    while ove:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    # Appending and reading from LeaderboardT.txt before the leaderboard function is called so data is ready to be displayed
                    # a+ Opens file for both reading and appending
                    file = open("leaderboardT.txt","a+")
                    file.write(str(username) + "," + (str(score)) + "\n");

                    # the seek() method changes the current file position back to the top so it can be read from the begining again
                    file.seek(0)

                    # Numlines is used to find the range of how many elements need to be blitted later on in the leaderboard
                    numLines = 0
                    leaderboardTuple = []

                    for line in file:
                        data = line.split(",")
                        usernameL = data[0]
                        scoreL = data[1]
                        scoreL = scoreL.strip('\n')
                        leaderboardTuple.append((usernameL, int(scoreL)))

                        numLines += 1


                    # Only the top 10 are displayed
                    if numLines > 10:
                        numLines = 10

                    print(Sort_Tuple(leaderboardTuple))

                    print(numLines)
                    file.close()

                    leaderboardTuple = Sort_Tuple(leaderboardTuple)
                    game_leaderboard(font,WHITE,BLACK,WIDTH,HEIGHT,clock,screen,Star,username,score,leaderboardTuple,numLines)
                    ove = False




        screen.fill(BLACK)


        overText = font.render('Game Over', True, (WHITE))
        overTextW = overText.get_width()
        screen.blit(overText,((WIDTH-overTextW)/2,(HEIGHT)/2))

        for i in range (1,20):
            newStarx = random.randint(1, WIDTH)
            newStary = random.randint(1, HEIGHT)
            newstarDifficult = Star(screen, WHITE, (newStarx, newStary), random.randint(1, 2), 20)


        pygame.display.update()
        clock.tick(15)


def Sort_Tuple(leaderboardTuple):
    leaderboardTuple.sort(key = lambda x: x[1],reverse= True)
    return leaderboardTuple
    
