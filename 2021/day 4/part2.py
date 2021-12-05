from part1 import BingoBoard, parseInput


def last_winner(numbers, bingo_boards):
    winners = []
    combos = []
    for num in numbers:
        for index, board in enumerate(bingo_boards):
            board.draw(num)
            if board.is_winner() and index not in winners:
                winners.append(index)
                combos.append(num * board.score())
    return combos[-1]


if __name__ == "__main__":
    numbers, bingo_boards = parseInput("input.txt")
    print(last_winner(numbers, bingo_boards))
