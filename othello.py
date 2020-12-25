import sys

import pygame.mixer
from pygame.locals import *
from board import Board
from AI import State, minimax, select_action


class Game:
    def __init__(self):
        pygame.init()
        self.board_size = 8
        self.screen_size = 600, 600
        self.board = Board(self.board_size)
        self.menu_activated = False
        self.finished = False
        self.screen = pygame.display.set_mode(self.screen_size)
        self.bg = pygame.image.load("assets/img/board.png")
        self.black_disk_pic = pygame.image.load("assets/img/black.png")
        self.white_disk_pic = pygame.image.load("assets/img/white.png")
        self.white_disk_pic_hint = pygame.image.load("assets/img/white2.png")
        self.black_disk_pic_hint = pygame.image.load("assets/img/black2.png")
        self.menu_icon = pygame.image.load("assets/img/menu_icon.png")
        self.menu = pygame.image.load("assets/img/menu.png")
        self.GAME_FONT = pygame.font.Font("freesansbold.ttf", 24)

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
        if self.menu_activated:
            self.screen.blit(self.menu, (200, 200))
        black_score = self.GAME_FONT.render("Black: {}".format(self.board.black), False, (0, 0, 0))
        white_score = self.GAME_FONT.render("White: {}".format(self.board.white), False, (0, 0, 0))
        self.screen.blit(black_score, (180, 550))
        self.screen.blit(white_score, (320, 550))

    def handle_event(self):
        if self.board.player == 'white':
            # print("FUCK U")
            import time
            state = State()
            print("sdfsdfsdfsdfsd")
            start_time = time.time()
            state.board = self.board
            minimax(state, True, 5, -10000000, 10000000)
            State.all_states = dict()
            print(time.time() - start_time)
            try:
                next_state = select_action(state)
                insert_i = next_state[1][0]
                insert_j = next_state[1][1]
                # print(insert_i, insert_j)
                insert = (insert_i, insert_j)
                white, black = self.board.handle_board_changes(insert)
                if self.board.is_game_finished:
                    self.menu_activated = True
                    self.finished = True
                    print("finished white: {}, black: {}".format(white, black))
            except:
                print('err')



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

                if self.menu_activated:
                    if insert_i == 3 and insert_j in [3, 4] and not self.finished:
                        self.menu_activated = False
                    elif insert_i == 4 and insert_j in [3, 4]:
                        del self.board
                        self.board = Board(self.board_size)
                        self.menu_activated = False
                else:
                    if insert_i == -1 and insert_j == 7:
                        self.menu_activated = True
                    elif 0 <= insert_j < 8 and 0 <= insert_i < 8:
                        if self.board.player == 'black':
                            white, black = self.board.handle_board_changes((insert_i, insert_j))
                            if self.board.is_game_finished:
                                self.menu_activated = True
                                self.finished = True
                                print("finished white: {}, black: {}".format(white, black))
                        # elif self.board.player == 'white':
                        #     # print("FUCK U")
                        #     import time
                        #     state = State()
                        #     print("sdfsdfsdfsdfsd" )
                        #     start_time = time.time()
                        #     state.board = self.board
                        #     minimax(state, True, 5, -10000000, 10000000)
                        #     State.all_states = dict()
                        #     print(time.time() - start_time)
                        #     next_state = select_action(state)
                        #     insert_i = next_state[1][0]
                        #     insert_j = next_state[1][1]
                        #     # print(insert_i, insert_j)
                        #     insert = (insert_i, insert_j)
                        #     self.board.handle_board_changes(insert)


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
