import pygame
import os
pygame.font.init()

SCREEN_WIDTH = 540
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)
WHITE_GREY = (220, 220, 220)
BLUE = (0, 0, 255)

def hover(x, y, width, height):
    mouse = pygame.mouse.get_pos()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        return True
    return False


def post_game_menu(win, outcome, play_time, strikes):
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(win, GREY, (70, 80, 400, 440))
    fnt = pygame.font.SysFont("comicsans", 70)
    outcome_text = fnt.render("You " + outcome + "!", 1, BLACK)
    text_rect = outcome_text.get_rect(center=(SCREEN_WIDTH/2, 165))
    win.blit(outcome_text, text_rect)

    fnt = pygame.font.SysFont("comicsans", 30)
    time_text = fnt.render("Time: " + str(play_time), 1, BLACK)
    text_rect = time_text.get_rect(center=(SCREEN_WIDTH/2, 260))
    win.blit(time_text, text_rect)

    strike_text = fnt.render("Mistakes: " + str(strikes), 1, BLACK)
    text_rect = strike_text.get_rect(center=(SCREEN_WIDTH/2, 300))
    win.blit(strike_text, text_rect)

    if hover(100, 380, 150, 50):
        pygame.draw.rect(win, WHITE_GREY, (100, 380, 150, 50))
        pygame.draw.lines(win, BLACK, True, [(100, 380), (250, 380), (250, 430), (100, 430)], 3)
        if click[0] == 1:
            print("main menu button clicked")
    else:
        pygame.draw.rect(win, WHITE, (100, 380, 150, 50))
        pygame.draw.lines(win, WHITE, True, [(100, 380), (250, 380), (250, 430), (100, 430)], 3)

    if hover(290, 380, 150, 50):
        pygame.draw.rect(win, WHITE_GREY, (290, 380, 150, 50))
        pygame.draw.lines(win, BLACK, True, [(290, 380), (440, 380), (440, 430), (290, 430)], 3)
        if click[0] == 1:
            pygame.quit()
            exit()
    else:
        pygame.draw.rect(win, WHITE, (290, 380, 150, 50))
        pygame.draw.lines(win, WHITE, True, [(290, 380), (440, 380), (440, 430), (290, 430)], 3)

    play_again_text = fnt.render("Play Again", 1, BLACK)
    text_rect = play_again_text.get_rect(center=(175, 405))
    win.blit(play_again_text, text_rect)

    quit_text = fnt.render("Quit", 1, BLACK)
    text_rect = quit_text.get_rect(center=(365, 405))
    win.blit(quit_text, text_rect)

    pygame.draw.rect(win, WHITE_GREY, (75, 500, 95, 15))
    fnt = pygame.font.SysFont("comicsans", 20)
    if hover(75, 500, 95, 15):
        view_board_text = fnt.render("<- View Board", 1, BLUE)
        win.blit(view_board_text, (79, 500))
    else:
        view_board_text = fnt.render("<- View Board", 1, BLACK)
        win.blit(view_board_text, (79, 500))

    pygame.display.flip()


def main():

    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")
    win.fill(WHITE)
    post_game_menu(win, "Win", 160, 2)
    run = True
    while run:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        post_game_menu(win, "Win", 160, 2)


main()
pygame.quit()
