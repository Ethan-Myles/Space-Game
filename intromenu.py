import pygame
import random
from textbox import Textbox


def game_intro(WIDTH, HEIGHT, screen, BLACK, WHITE, font, Star, clock):
    intro = True

    textObject = Textbox((WIDTH - 200) / 2, 340, 200, 24, 24, 20, True, "", (0, 191, 255), (255, 255, 255),(0, 191, 255))

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    username = textObject.getName()
                    intro = False
                    return username

            textObject.handle_event(event)

        screen.fill(BLACK)

        # all_sprites_list.add(elementBox)

        textObject.update()
        textObject.draw(screen)
        menuText = font.render('Welcome to the Periodic Table Quiz', True, (WHITE))
        menuTextW = menuText.get_width()
        screen.blit(menuText, ((WIDTH - menuTextW) / 2, 222))

        # Background stars
        for i in range(1, 20):
            newStarx = random.randint(1, WIDTH)
            newStary = random.randint(1, HEIGHT)
            newstarIntro = Star(screen, WHITE, (newStarx, newStary), random.randint(1, 2), 20)

        pygame.display.update()
        clock.tick(15)
