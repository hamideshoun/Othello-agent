from board import Board
import copy
import time


class State:
    def __init__(self):
        self.board = Board(8)
        self.heuristic = 0
        self.next_states = []


def minimax(state, turn, depth, alpha, beta):
    if depth == 0 or state.board.is_game_finished:
        return state.board.white - state.board.black
    if turn:
        actions = state.board.get_selectable_index('white')
        max_eval = -10000
        for action in actions:
            # creating child state with copy of parent board
            child_state = State()
            copy_board = copy.deepcopy(state.board)
            copy_board.handle_board_changes(action)
            child_state.board = copy_board
            # updating children list of current state
            state.next_states.append([child_state, action])
            # calculating heuristic of child state
            temp_eval = minimax(child_state, False, depth-1, alpha, beta)
            max_eval = max(max_eval, max_eval)
            # pruning
            alpha = max(alpha, temp_eval)
            if alpha >= beta:
                break
        # assigning maximum heuristic of children to heuristic of parent state
        state.heuristic = max_eval
        # print("MAX :  " + state.heuristic.__str__() + " in depth : " + depth.__str__())
        return max_eval

    if not turn:
        actions = state.board.get_selectable_index('black')
        min_eval = 10000
        for action in actions:
            # creating child state with copy of parent board
            child_state = State()
            copy_board = copy.deepcopy(state.board)
            copy_board.handle_board_changes(action)
            child_state.board = copy_board
            # updating children list of current state
            state.next_states.append([child_state, action])
            # calculating heuristic of child state
            temp_eval = minimax(child_state, True, depth-1, alpha, beta)
            min_eval = min(min_eval, temp_eval)
            # pruning
            beta = min(beta, min_eval)
            if alpha >= beta:
                break
        # assigning minimum heuristic of children to heuristic of parent state
        state.heuristic = min_eval
        # print("MIN :  " + state.heuristic.__str__() + " in depth : " + depth.__str__())
        return min_eval


def select_action(state):
    if not state.next_states:
        return
    next_state = state.next_states[0]
    for ns in state.next_states:
        if ns[0].heuristic > next_state[0].heuristic:
            next_state = ns
    print(next_state)
    return next_state




