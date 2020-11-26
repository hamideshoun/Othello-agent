import sys

import pygame.mixer
from pygame.locals import *


class Disk:
    def __init__(self, color, x, y, allowed):
        self.color = color
        self.x = x
        self.y = y
        self.allowed = allowed


class Board:
    def __init__(self, board_arr):
        self.board_arr = board_arr
        board_arr[3][3].color = 'white'
        board_arr[3][4].color = 'black'
        board_arr[4][3].color = 'black'
        board_arr[4][4].color = 'white'


# INITIALS:
board_size = 8
screen_size = width, height = 600, 600
turn = 'black'
arr = [[Disk('none', 26 + (i * 70), 26 + (j * 70), False) for j in range(board_size)] for i in range(board_size)]
board = Board(arr)


def flip(direction, position):
    """ Flips (capturates) the pieces of the given color in the given direction
    (1=North,2=Northeast...) from position. """

    if direction == 1:
        # north
        row_inc = -1
        col_inc = 0
    elif direction == 2:
        # northeast
        row_inc = -1
        col_inc = 1
    elif direction == 3:
        # east
        row_inc = 0
        col_inc = 1
    elif direction == 4:
        # southeast
        row_inc = 1
        col_inc = 1
    elif direction == 5:
        # south
        row_inc = 1
        col_inc = 0
    elif direction == 6:
        # southwest
        row_inc = 1
        col_inc = -1
    elif direction == 7:
        # west
        row_inc = 0
        col_inc = -1
    elif direction == 8:
        # northwest
        row_inc = -1
        col_inc = -1

    places = []  # pieces to flip
    i = position[0] + row_inc
    j = position[1] + col_inc

    if turn == 'white':
        other = 'black'
    else:
        other = 'white'

    if i in range(8) and j in range(8) and board.board_arr[i][j].color == other:
        # assures there is at least one piece to flip
        places = places + [(i, j)]
        i = i + row_inc
        j = j + col_inc
        while i in range(8) and j in range(8) and board.board_arr[i][j].color == other:
            # search for more pieces to flip
            places = places + [(i, j)]
            i = i + row_inc
            j = j + col_inc
        if i in range(8) and j in range(8) and board.board_arr[i][j].color == turn:
            # found a piece of the right color to flip the pieces between
            print(places)
            for pos in places:
                # flips
                board.board_arr[pos[0]][pos[1]].color = turn


# FUNCTIONS:
def allowed_squares():
    global turn
    pass


def win_check():
    pass


def insert_disk(board, insert_i, insert_j):
    pass


def render_board():
    for i in range(board_size):
        for j in range(board_size):
            if board.board_arr[i][j].color == 'black':
                screen.blit(black_disk_pic, (board.board_arr[i][j].x, board.board_arr[i][j].y))
            if board.board_arr[i][j].color == 'white':
                screen.blit(white_disk_pic, (board.board_arr[i][j].x, board.board_arr[i][j].y))


def handle_event():
    global turn
    for event in pygame.event.get():
        # QUIT:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            sys.exit()

        # MOUSE CLICK:
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            insert_i = (mouse_x - 26) // 70
            insert_j = (mouse_y - 26) // 70
            if board.board_arr[insert_i][insert_j].color == 'none':
                board.board_arr[insert_i][insert_j].color = turn
                print(turn, insert_i, insert_j)
                for i in range(1, 9):
                    flip(i, (insert_i, insert_j))
                if turn == 'black':
                    turn = 'white'
                else:
                    turn = 'black'

# MAIN:
# MAKING GAME:

pygame.init()

screen = pygame.display.set_mode(screen_size)

bg = pygame.image.load("assets/img/board.png")
black_disk_pic = pygame.image.load("assets/img/black.png")
white_disk_pic = pygame.image.load("assets/img/white.png")

# GAME LOOP:
while True:
    screen.blit(bg, (0, 0))

    # EVENTS:
    handle_event()



    allowed_squares()

    # RENDERING DISKS IN BOARD:
    render_board()

    win_check()
    pygame.display.flip()
