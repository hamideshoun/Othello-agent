class Disk:
    def __init__(self, color, x, y, allowed):
        self.color = color
        self.x = x
        self.y = y
        self.allowed = allowed


class Board:
    def __init__(self, board_size):
        self.player = 'black'
        self.board_arr = [[Disk('none', 26 + (i * 70), 26 + (j * 70), False) for j in range(board_size)] for i in
                          range(board_size)]
        self.board_arr[3][3].color = 'white'
        self.board_arr[3][4].color = 'black'
        self.board_arr[4][3].color = 'black'
        self.board_arr[4][4].color = 'white'

    def get_opponent(self):
        turn = self.player
        if turn == 'black':
            return 'white'
        else:
            return 'black'

    def make_flip(self, position):
        for direction in range(1, 9):
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

            other = self.get_opponent()

            if i in range(8) and j in range(8) and self.board_arr[i][j].color == other:
                # assures there is at least one piece to flip
                places = places + [(i, j)]
                i = i + row_inc
                j = j + col_inc
                while i in range(8) and j in range(8) and self.board_arr[i][j].color == other:
                    places = places + [(i, j)]
                    i = i + row_inc
                    j = j + col_inc
                if i in range(8) and j in range(8) and self.board_arr[i][j].color == self.player:
                    for pos in places:
                        # flips
                        self.board_arr[pos[0]][pos[1]].color = self.player

    def set_color(self, position):
        insert_i, insert_j = position
        if self.board_arr[insert_i][insert_j].color == 'none':
            self.board_arr[insert_i][insert_j].color = self.player

    def change_player(self):
        self.player = self.get_opponent()

    def handle_board_changes(self, position):
        self.set_color(position)
        self.make_flip(position)
        self.change_player()
