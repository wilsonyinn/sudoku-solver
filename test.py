import pygame
import os
pygame.font.init()

def main_menu(win):
    
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    title_text = fnt.render("SUDOKU", 1, (0, 0, 0))
    win.blit(title_text, (540 - 160, 560))
    
    mode_text1 = fnt.render("EASY", 1, (0, 0, 0))
    mode_text2 = fnt.render("MEDIUM", 1, (0, 0, 0))
    mode_text3 = fnt.render("HARD", 1, (0, 0, 0))
    pygame.draw.rect(win, (0, 0, 0), (270, 350, 100, 50))
    pygame.draw.rect(win, (0, 0, 0), (270, 400, 100, 50))
    win.blit(mode_text1, (20, 560))
    win.blit(mode_text2, (20, 560))
    win.blit(mode_text3, (20, 560))
    # Draw grid and board
def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    main_menu(win)
    run = True
    while run:
        pygame.display.update()

main()
pygame.quit()

    
