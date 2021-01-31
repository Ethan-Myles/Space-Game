import pygame
import random



def game_difficulty(screen,BLACK,WHITE,BLUE,font,WIDTH,HEIGHT,Star,clock):
    dif = True


    while dif:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    dif = False
                    return selection

# === mouse y coordinates change colour of text ===
        m = pygame.mouse.get_pos()
        
        if m[1] >= 320 and m[1] <=345:
            colourChangeD = BLUE
            selection = "Difficult"
        else:
          colourChangeD = WHITE

        if m[1] >= 420 and m[1] <=445:
            colourChangeM = BLUE
            selection = "Medium"
        else:
          colourChangeM = WHITE

        if m[1] >= 520 and m[1] <=554:
            colourChangeE = BLUE
            selection = "Easy"
        else:
          colourChangeE = WHITE

        screen.fill(BLACK)

        # Difficulty - title text
        levelText = font.render('Level select', True, (WHITE))
        levelTextW = levelText.get_width()
        screen.blit(levelText,((WIDTH-levelTextW)/2,222))

        # Difficulty - difficult text
        difficultText = font.render('Difficult', True, (colourChangeD))
        difficultTextW = difficultText.get_width()
        screen.blit(difficultText,((WIDTH-difficultTextW)/2,322))

        # Difficulty - medium text
        mediumText = font.render('Medium', True, (colourChangeM))
        mediumTextW = mediumText.get_width()
        screen.blit(mediumText,((WIDTH-mediumTextW)/2,422))

        # Difficulty - easy text
        easyText = font.render('Easy', True, (colourChangeE))
        easyTextW = easyText.get_width()
        screen.blit(easyText,((WIDTH-easyTextW)/2,522))

        # Background stars
        for i in range (1,21):
            newStarx = random.randint(1, WIDTH)
            newStary = random.randint(1, HEIGHT)
            newstarDifficult = Star(screen, WHITE, (newStarx, newStary), random.randint(1, 2), 20)

        #surface6 = pygame.Surface([400,100])
        #difficultBox = Difficultbox(surface6, WHITE, 400, 100)
        #all_sprites_list.add(difficultBox)


        pygame.display.update()
        clock.tick(15)
