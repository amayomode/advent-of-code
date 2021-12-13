pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def auto_complete(chunk):
    stack = []
    for char in chunk:
        if char in pairs.keys():
            stack.append(char)
        else:
            if not stack:
                return 0
            top = stack.pop()
            if pairs[top] != char:
                return 0
    complete = [pairs[c] for c in stack[::-1]]
    return complete


def score_sequence(complete):
    score = 0
    for char in complete:
        score = score * 5 + table[char]
    return score


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        scores = []
        for line in f.readlines():
            complete = auto_complete(line.strip())
            if complete:
                scores.append(score_sequence(complete))
        scores.sort()
        print(scores[len(scores)//2])
