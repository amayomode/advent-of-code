pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def first_mismatch(chunk):
    stack = []
    for char in chunk:
        if char in pairs.keys():
            stack.append(char)
        else:
            if not stack:
                return char
            top = stack.pop()
            if pairs[top] != char:
                return char
    return 0


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        score = 0
        for line in f.readlines():
            mismatch = first_mismatch(line.strip())
            if mismatch:
                score += table[mismatch]
        print(score)
