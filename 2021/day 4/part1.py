import numpy as np


class BingoBoard:
    def __init__(self, board):
        self.board = np.array(board)
        self.mask = np.full(self.board.shape, False, dtype=bool)

    def draw(self, number):
        location = np.where(self.board == number)
        for cord in zip(location[0], location[1]):
            self.mask[cord] = True

    def is_winner(self):
        rows, cols = self.mask.shape
        for i in range(rows):
            if all(self.mask[i, :] != False):
                return True
        for j in range(cols):
            if all(self.mask[:, j] != False):
                return True
        return False

    def score(self):
        return (self.board[~self.mask]).sum()


def first_winner(numbers, bingo_boards):
    for num in numbers:
        for board in bingo_boards:
            board.draw(num)
            if board.is_winner():
                return num * board.score()
    return 0


def parseInput(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        numbers = [int(i) for i in lines[:1][0].strip().split(",")]
        bingo_boards = []
        temp = []
        for line in lines[3:]:
            if line == "\n":
                bingo_boards.append(BingoBoard(temp))
                temp = []
                continue
            temp.append([int(i) for i in line.strip().split()])
        return numbers, bingo_boards


if __name__ == "__main__":
    numbers, bingo_boards = parseInput("input.txt")
    print(first_winner(numbers, bingo_boards))
