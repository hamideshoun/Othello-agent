import random

from board import Board
import copy
import time


class Agent:
    all_states = dict()

    def __init__(self, co_f=1, co_g=1, co_h=1):
        self.board = Board(8)
        self.heuristic = 0
        self.next_states = []
        self.co_f = co_f
        self.co_g = co_g
        self.co_h = co_h

    def minimax(self, turn, depth, alpha, beta):
        # board_hash = state.board.create_hash(turn)
        # if board_hash in State.all_states:
        #     state.heuristic = State.all_states[board_hash]
        #     return State.all_states[board_hash]

        white_selectable = self.board.get_selectable_index('white')
        black_selectable = self.board.get_selectable_index('black')
        if depth == 0 or (not white_selectable and not black_selectable):
            return self.calculate_heuristic()
        if turn:
            actions = white_selectable
            max_eval = -10000
            for action in random.choices(list(actions), k=min(len(actions), 6)):
                # creating child state with copy of parent board
                child_state = Agent()
                copy_board = copy.deepcopy(self.board)
                copy_board.handle_board_changes(action)
                child_state.board = copy_board
                # updating children list of current state
                self.next_states.append([child_state, action])
                # calculating heuristic of child state
                temp_eval = child_state.minimax(False, depth - 1, alpha, beta)
                max_eval = max(max_eval, temp_eval)
                # pruning
                alpha = max(alpha, max_eval)
                if alpha >= beta:
                    break
            # assigning maximum heuristic of children to heuristic of parent state
            self.heuristic = max_eval
            # print("MAX :  " + state.heuristic.__str__() + " in depth : " + depth.__str__())
            # State.all_states[board_hash] = max_eval
            return max_eval

        if not turn:
            actions = black_selectable
            min_eval = 10000
            for action in random.choices(list(actions), k=min(len(actions), 6)):
                # creating child state with copy of parent board
                child_state = Agent()
                copy_board = copy.deepcopy(self.board)
                copy_board.handle_board_changes(action)
                child_state.board = copy_board
                # updating children list of current state
                self.next_states.append([child_state, action])
                # calculating heuristic of child state
                temp_eval = child_state.minimax(True, depth - 1, alpha, beta)
                min_eval = min(min_eval, temp_eval)
                # pruning
                beta = min(beta, min_eval)
                if alpha >= beta:
                    break
            # assigning minimum heuristic of children to heuristic of parent state
            self.heuristic = min_eval
            # State.all_states[board_hash] = min_eval
            # print("MIN :  " + state.heuristic.__str__() + " in depth : " + depth.__str__())
            return min_eval

    def corners(self):
        corner = 0
        if self.board.board_arr[0][0].color == 'white':
            corner += 1
        if self.board.board_arr[0][7].color == 'white':
            corner += 1
        if self.board.board_arr[7][0].color == 'white':
            corner += 1
        if self.board.board_arr[7][7].color == 'white':
            corner += 1
        if self.board.board_arr[0][0].color == 'black':
            corner -= 1
        if self.board.board_arr[0][7].color == 'black':
            corner -= 1
        if self.board.board_arr[7][0].color == 'black':
            corner -= 1
        if self.board.board_arr[7][7].color == 'black':
            corner -= 1
        return corner

    def borders(self):
        border = 0
        for i in range(0, 8):
            if self.board.board_arr[0][i].color == 'white':
                border += 1
            if self.board.board_arr[0][i].color == 'black':
                border -= 1
            if self.board.board_arr[7][i].color == 'white':
                border += 1
            if self.board.board_arr[7][i].color == 'black':
                border -= 1

        for j in range(0, 8):
            if self.board.board_arr[j][0].color == 'white':
                border += 1
            if self.board.board_arr[j][0].color == 'black':
                border -= 1
            if self.board.board_arr[j][7].color == 'white':
                border += 1
            if self.board.board_arr[j][7].color == 'black':
                border -= 1
        return border

    def calculate_heuristic(self):
        f = self.board.white - self.board.black
        g = self.corners()
        h = self.borders()
        return self.co_f * f + self.co_g * g + self.co_h * h


def select_action(state, turn):
    if not state.next_states:
        return
    next_state = state.next_states[0]
    if turn == 'white':
        for ns in state.next_states:
            if ns[0].heuristic > next_state[0].heuristic:
                next_state = ns
    if turn == 'black':
        for ns in state.next_states:
            if ns[0].heuristic > next_state[0].heuristic:
                next_state = ns
    return next_state










