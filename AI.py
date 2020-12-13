from board import Board


class State:
    def __init__(self):
        self.board = Board()
        self.heuristic = 0



def minimax(state, turn, depth):
    actions = []
    actions = state.board.get_selectable_index()

    if depth == 0:
        return state.board.white - state.board.black

    if turn:
        max_eval = -10000
        for action in actions:
            child_state = State()
            copy_board = state.board
            copy_board.handle_board_changes(action)
            child_state.board = copy_board
            temp_eval = minimax(child_state, False, depth-1)
            max_eval = max(max_eval, temp_eval)
        return max_eval

    if not turn:
        max_eval = 10000
        for action in actions:
            child_state = State()
            copy_board = state.board
            copy_board.handle_board_changes(action)
            child_state.board = copy_board
            temp_eval = minimax(child_state, True, depth-1)
            max_eval = max(max_eval, temp_eval)
        return max_eval
