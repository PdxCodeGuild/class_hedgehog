from importlib import invalidate_caches
import random


class Player:
    def __init__(self, name, token):
        self.token = token
        self.name = name
        self.num_of_wins = 0

# Class for game board


class Board:
    def __init__(self):
        self.board = ["___", "___", "___"]
        self.current_player = None
        self.turn_counter = 0

    # select random spot
    def pick_random(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if self.check_available(row, col):
            return row, col
        return self.pick_random()

    def check_available(self, row, col):
        if self.board[row][col] == "_":
            return True
        else:
            return False

    def check_win(self):
        for row in self.board:
            if self.current_player.token == row[0] == row[1] == row[2]:
                return True
        for col in range(3):
            if self.current_player.token == self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return True
        if self.current_player.token == self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.current_player.token == self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

        return False

    def place_token(self, row, col):
        plane = list(self.board[row])
        plane[col] = self.current_player.token
        plane = "".join(plane)
        self.board[row] = plane

        return self.board

    def __str__(self):
        return "\n".join(self.board)


def get_token(prev_token=None):
    while True:
        invalid = ["_", "", " "]
        token = input("-> ") + " "
        if token[0] == prev_token:
            continue
        if token[0] not in invalid:
            break

    return token[0]


board = Board()
name = input("Enter your name: ")
print(f"Pick a token {name}")
token = get_token()
print("Pick a rival token")
comp_token = get_token(token)
p1 = Player(name, token)
comp = Player("Rival", comp_token)

players = [p1, comp]

random.shuffle(players)
board.current_player = players[0]
while not board.check_win() and board.turn_counter < 9:
    board.current_player = players[board.turn_counter % 2]
    print(board.current_player.name + "'s turn.")

    if board.current_player.name == "Rival":
        row, col = board.pick_random()
        board.place_token(row, col)

    else:
        while True:
            row = int(input("Pick a row 0-2: "))
            col = int(input("Pick a column 0-2: "))
            if board.check_available(row, col):
                board.place_token(row, col)
                break

    board.turn_counter += 1
    print(board)

if board.turn_counter == 9 and not board.check_win():
    print("Cat game (DRAW)")
else:
    print(board.current_player.name + " wins")
