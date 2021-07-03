import pygame
import os
pygame.font.init()

SCREEN_WIDTH = 540
SCREEN_HEIGHT = 600
GREY = (192, 192, 192)
WHITE = (255, 255, 255)
WHITE_GREY = (220, 220, 220)

def button(win):
    fnt = pygame.font.SysFont("comicsans", 40)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(mouse)
    print(click)
    if SCREEN_WIDTH/2 - 75 < mouse[0] < SCREEN_WIDTH/2 - 75 + 150 and 210 < mouse[1] < 270:
        pygame.draw.rect(win, WHITE_GREY, pygame.Rect(
        SCREEN_WIDTH/2 - 75, 210, 150, 60))
        if click[0] == 1:
            difficulty = "easy"

    else:
        pygame.draw.rect(win, WHITE, pygame.Rect(
        SCREEN_WIDTH/2 - 75, 210, 150, 60))
    if SCREEN_WIDTH/2 - 75 < mouse[0] < SCREEN_WIDTH/2 - 75 + 150 and 310 < mouse[1] < 370:
        pygame.draw.rect(win, WHITE_GREY, pygame.Rect(
        SCREEN_WIDTH/2 - 75, 310, 150, 60))
        if click[0] == 1:
            difficulty = "medium"
    else:
        pygame.draw.rect(win, WHITE, pygame.Rect(
        SCREEN_WIDTH/2 - 75, 310, 150, 60))    
    if SCREEN_WIDTH/2 - 75 < mouse[0] < SCREEN_WIDTH/2 - 75 + 150 and 410 < mouse[1] < 470:
        pygame.draw.rect(win, WHITE_GREY, pygame.Rect(
        SCREEN_WIDTH/2 - 75, 410, 150, 60))
        if click[0] == 1:
            difficulty = "hard"
    else:
        pygame.draw.rect(win, WHITE, pygame.Rect(
        SCREEN_WIDTH/2 - 75, 410, 150, 60))  


    mode_text1 = fnt.render("EASY", 1, (0, 0, 0))
    mode_text2 = fnt.render("MEDIUM", 1, (0, 0, 0))
    mode_text3 = fnt.render("HARD", 1, (0, 0, 0))
    text_rect = mode_text1.get_rect(center=(SCREEN_WIDTH/2, 240))
    win.blit(mode_text1, text_rect)
    text_rect = mode_text2.get_rect(center=(SCREEN_WIDTH/2, 340))
    win.blit(mode_text2, text_rect)
    text_rect = mode_text3.get_rect(center=(SCREEN_WIDTH/2, 440))
    win.blit(mode_text3, text_rect)

def main_menu(win):

    # Draw time
    fnt = pygame.font.SysFont("comicsans", 60)
    title_text = fnt.render("SUDOKU", 1, (0, 0, 0))
    text_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, 100))
    win.blit(title_text, text_rect)
    
    button(win)
    pygame.display.flip()
    # Draw grid and board


def main():

    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")
    win.fill(GREY)
    main_menu(win)
    run = True
    while run:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        main_menu(win)


main()
pygame.quit()
