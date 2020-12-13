from board import Board


class State:
    def __init__(self):
        self.board = Board()
        self.heuristic = 0
        self.next_states = []


def minimax(state, turn, depth, alpha, beta):
    actions = state.board.get_selectable_index()
    if depth == 0:
        return state.board.white - state.board.black

    if turn:
        max_eval = -10000
        for action in actions:
            # creating child state with copy of parent board
            child_state = State()
            copy_board = state.board
            copy_board.handle_board_changes(action)
            child_state.board = copy_board
            # updating children list of current state
            state.next_states.append(child_state)
            # calculating heuristic of child state
            temp_eval = minimax(child_state, False, depth-1, alpha, beta)
            max_eval = max(max_eval, temp_eval)
            # pruning
            alpha = max(alpha, temp_eval)
            if alpha >= beta:
                break
        # assigning maximum heuristic of children to heuristic of parent state
        state.heuristic = max_eval
        return max_eval

    if not turn:
        min_eval = 10000
        for action in actions:
            # creating child state with copy of parent board
            child_state = State()
            copy_board = state.board
            copy_board.handle_board_changes(action)
            child_state.board = copy_board
            # updating children list of current state
            state.next_states.append(child_state)
            # calculating heuristic of child state
            temp_eval = minimax(child_state, True, depth-1, alpha, beta)
            min_eval = max(min_eval, temp_eval)
            # pruning
            beta = max(beta, temp_eval)
            if alpha >= beta:
                break
        # assigning minimum heuristic of children to heuristic of parent state
        state.heuristic = min_eval
        return min_eval


def select_action(state):
    next_state = state.next_states[0]
    for ns in state.next_states:
        if ns.heuristic > next_state.heuristic:
            next_state = ns
    return state.next_states.index(next_state)

