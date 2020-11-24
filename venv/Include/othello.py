import sys, pygame, pygame.mixer
from pygame.locals import *

#INITIALS:
board_size = 8
screen_size = width, height = 600, 600
turn = 'black'

#OBJECTS: DISK, BOARD
class disk:
    def __init__(self, color, x, y, allowed):
        self.color = color
        self.x = x
        self.y = y
        self.allowed = allowed

class board:
    def __init__(self, board_arr):
        self.board_arr = board_arr
        board_arr[3][3].color = 'white'
        board_arr[3][4].color = 'black'
        board_arr[4][3].color = 'black'
        board_arr[4][4].color = 'white'


#FUNCTIONS:
def allowed_squares(board, turn):
    pass

def win_check(board):
    pass

def insert_disk(board, insert_i, insert_j):
    pass



#MAIN:
#MAKING GAME:
arr=[]
for i in range(board_size):
    col = []
    for j in range(board_size):
        temp = disk('none', 26 + (i * 70), 26 + (j * 70), False)
        col.append(temp)
    arr.append(col)

board = board(arr)


pygame.init()

screen = pygame.display.set_mode(screen_size)

bg = pygame.image.load("assets/img/board.png")
black_disk_pic = pygame.image.load("assets/img/black.png")
white_disk_pic = pygame.image.load("assets/img/white.png")


#GAME LOOP:
while 1:
    screen.blit(bg, (0, 0))

    #EVENTS:
    for event in pygame.event.get():
        #QUIT:
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()
        elif event.type == KEYDOWN and event.key == K_q: sys.exit()

        #MOUSE CLICK:
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            insert_i = (mouse_x - 26) // 70
            insert_j = (mouse_y - 26) // 70
            if board.board_arr[insert_i][insert_j].color == 'none':
                board.board_arr[insert_i][insert_j].color = turn
                if turn == 'black': turn = 'white'
                else: turn = 'black'



    #RENDERING DISKS IN BOARD:
    for i in range(board_size):
        for j in range(board_size):
            if board.board_arr[i][j].color == 'black':
                screen.blit(black_disk_pic, (board.board_arr[i][j].x, board.board_arr[i][j].y))
            if board.board_arr[i][j].color == 'white':
                screen.blit(white_disk_pic, (board.board_arr[i][j].x, board.board_arr[i][j].y))



    pygame.display.flip()