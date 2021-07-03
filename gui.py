from sudoku_solver import solve, valid
import pygame
import time
import random
from random import randint
pygame.font.init()


class Grid:
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # place holder board
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # we set the board based on difficulty with generate board function
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def __init__(self, row, col, width, height, difficulty):
        self.row = row
        self.col = col
        self.cubes = [[Cube(self.board[i][j], i, j, width, height)
                       for j in range(col)] for i in range(row)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None
        self.difficulty = difficulty

    def generate_board(self):
        # generate a valid solution grid
        # 1. generate the first 3x3 subsquare (currently no restraints)
        if self.difficulty == "easy":
            clear = 40
        elif self.difficulty == "medium":
            clear = 50
        elif self.difficulty == "hard":
            clear = 60
        rand_ints = random.sample(range(1, 10), 9)
        for i in range(3):
            for j in range(3):
                self.board[i][j] = rand_ints[len(rand_ints) - 1]
                rand_ints.pop()
        # 2 use the solve function to finish the rest of the board using backtracking
        solve(self.board)
        # erase some numbers based on difficulty
        for i in range(clear):
            x = randint(0, 8)
            y = randint(0, 8)
            self.board[x][y] = 0

        for i in range(9):
            for j in range(9):
                self.cubes[i][j].value = self.board[i][j]

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(
            self.col)] for i in range(self.row)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row, col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # draw grid lines
        gap = self.width/9
        for i in range(self.row+1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(win, (0, 0, 0), (0, i*gap),
                             (self.width, i*gap), thickness)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0),
                             (i * gap, self.height), thickness)
        # draw cubes
        for i in range(self.row):
            for j in range(self.col):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        # reset all other
        for i in range(self.row):
            for j in range(self.col):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    row = 9
    col = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2),
                            y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val



def redraw_window(win, board, time, strikes):
    win.fill((255, 255, 255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0, 0, 0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw(win)


def format_time(secs):
    sec = secs % 60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

"""def main_menu(win):
    win.fill((255, 255, 255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    title_text = fnt.render("SUDOKU", (0, 0, 0))
    win.blit(title_text, (540 - 160, 560))
    # Draw Strikes
    mode_text1 = fnt.render("EASY", (0, 0, 0))
    mode_text2 = fnt.render("MEDIUM", (0, 0, 0))
    mode_text3 = fnt.render("HARD", (0, 0, 0))
    pygame.draw.rect(win, (0, 0, 0), (270, 350, 100, 50))
    pygame.draw.rect(win, (0, 0, 0), (270, 400, 100, 50))
    pygame.draw.rect(win, (0, 0, 0), (270, 450, 100, 50))
    win.blit(mode_text1, (20, 560))
    win.blit(mode_text1, (20, 560))
    win.blit(mode_text1, (20, 560))
    # Draw grid and board
    #board.draw(win)"""

def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    #main_menu(win)
    difficulty = "easy"
    board = Grid(9, 9, 540, 540, difficulty)
    board.generate_board()
    board.update_model()
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


main()
pygame.quit()
