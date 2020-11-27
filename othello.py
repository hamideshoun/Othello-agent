import sys

import pygame.mixer
from pygame.locals import *
from board import Board


class Game:
    def __init__(self):
        pygame.init()
        self.board_size = 8
        self.screen_size = 600, 600
        self.board = Board(self.board_size)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.bg = pygame.image.load("assets/img/board.png")
        self.black_disk_pic = pygame.image.load("assets/img/black.png")
        self.white_disk_pic = pygame.image.load("assets/img/white.png")
        self.white_disk_pic_hint = pygame.image.load("assets/img/white2.png")
        self.black_disk_pic_hint = pygame.image.load("assets/img/black2.png")
        self.menu_icon = pygame.image.load("assets/img/menu_icon.png")
        self.menu = pygame.image.load("assets/img/menu.png")

    def render_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board.board_arr[i][j].color == 'black':
                    self.screen.blit(self.black_disk_pic, (self.board.board_arr[i][j].x, self.board.board_arr[i][j].y))
                if self.board.board_arr[i][j].color == 'white':
                    self.screen.blit(self.white_disk_pic, (self.board.board_arr[i][j].x, self.board.board_arr[i][j].y))
                if (i, j) in self.board.get_selectable_index(self.board.player):
                    if self.board.player == 'black':
                        self.screen.blit(self.black_disk_pic_hint, (self.board.board_arr[i][j].x, self.board.board_arr[i][j].y))
                    elif self.board.player == 'white':
                        self.screen.blit(self.white_disk_pic_hint, (self.board.board_arr[i][j].x, self.board.board_arr[i][j].y))
        self.screen.blit(self.menu_icon, (492, 7))

    def handle_event(self):
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
                insert_j = (mouse_x - 60) // 60
                insert_i = (mouse_y - 60) // 60
                print(insert_i, insert_j)
                self.board.handle_board_changes((insert_i, insert_j))

    def run(self):
        while True:
            self.screen.blit(self.bg, (0, 0))

            # EVENTS:
            self.handle_event()

            self.render_board()

            pygame.display.flip()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
