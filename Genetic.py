from AI import Agent, select_action
from board import Board
import random
import multiprocessing
import json


class Game:
    def __init__(self, player1, player2):
        self.b = Board(8)
        self.player1 = player1
        self.player2 = player2

    def play(self):
        print('Game Started')
        while True:

            if self.b.player == 'white':
                s1 = Agent(**self.player1)
                s1.board = self.b
                s1.minimax(True, 5, -10000000, 10000000)
                try:
                    next_state = select_action(s1, 'white')
                    insert_i = next_state[1][0]
                    insert_j = next_state[1][1]
                    insert = (insert_i, insert_j)
                    print('white', insert)
                    white, black = self.b.handle_board_changes(insert)
                    if self.b.is_game_finished:
                        break
                except:
                    break
                    pass

            if self.b.player == 'black':
                s2 = Agent(**self.player2)
                s2.board = self.b
                s2.minimax(False, 5, -10000000, 10000000)
                try:
                    next_state = select_action(s2, 'black')
                    insert_i = next_state[1][0]
                    insert_j = next_state[1][1]
                    insert = (insert_i, insert_j)
                    print('black', insert)

                    white, black = self.b.handle_board_changes(insert)
                    if self.b.is_game_finished:
                        break
                except:
                    break
                    pass
        if self.b.white > self.b.black:
            result = {'winner': 'white', 'player1': self.player1, 'player2': self.player2}
        elif self.b.black > self.b.white:
            result = {'winner': 'black', 'player1': self.player1, 'player2': self.player2}
        else:
            result = {'winner': 'equal', 'player1': self.player1, 'player2': self.player2}
        with open('results.json', 'a') as f:
            f.write(json.dumps(result) + '\n')

        print('Game End')


def main():
    players = []

    for i in range(40):
        co_f = random.randint(1, 100)
        co_g = random.randint(1, 100)
        co_h = random.randint(1, 100)
        players.append({'co_f': co_f, 'co_g': co_g, 'co_h': co_h})


    leagues = [[] for i in range(4)]
    leagues[0] = players[:10]
    leagues[1] = players[10:20]
    leagues[2] = players[20:30]
    leagues[3] = players[30:]

    games = []

    for l in range(4):
        for i in range(10):
            for j in range(i+1, 10):
                game = Game(player1=leagues[l][i], player2=leagues[l][j])
                games.append(game)

    print(len(games))
    for game in games:
        t = multiprocessing.Process(target=game.play)
        t.start()

if __name__ == '__main__':
    main()


