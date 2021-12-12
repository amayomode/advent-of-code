from typing import final


def unique_shared_values(signal_patterns):
    unique = {1: "", 4: "", 7: "", 8: ""}
    shared = {6: [], 5: []}
    for pattern in signal_patterns.strip().split():
        if len(pattern) == 2:
            unique[1] = pattern
        elif len(pattern) == 3:
            unique[7] = pattern
        elif len(pattern) == 4:
            unique[4] = pattern
        elif len(pattern) == 7:
            unique[8] = pattern
        elif len(pattern) == 6:
            shared[6].append(pattern)
        else:
            shared[5].append(pattern)
    return unique, shared


def find_unique_segments(unique, shared):
    unique_segments = {}
    unique_segments[(3, 7)] = set(unique[1])
    unique_segments[(1, 4)] = set(unique[4]) - set(unique[1])
    unique_segments[(2)] = set(unique[7]) - set(unique[1])
    unique_segments[(5, 6)] = set(unique[8]) - \
        set(unique[1] + unique[4] + unique[7])
    unique_segments[(3, 4, 5)] = set()
    for v in shared[6]:
        i = set(unique[8]) - set(v)
        unique_segments[(3, 4, 5)].add(*i)
    return unique_segments


def decode_display(signal_patterns):
    unique, shared = unique_shared_values(signal_patterns)
    unique_segments = find_unique_segments(unique, shared)
    final_display = [{0}] * 8
    final_display[2] = unique_segments[(2)]

    final_display[4] = unique_segments[(3, 4, 5)].intersection(
        unique_segments[(1, 4)])
    final_display[1] = unique_segments[(1, 4)] - final_display[4]

    final_display[3] = unique_segments[(3, 4, 5)].intersection(
        unique_segments[(3, 7)])
    final_display[7] = unique_segments[(3, 7)] - final_display[3]

    final_display[5] = unique_segments[(3, 4, 5)].intersection(
        unique_segments[(5, 6)])
    final_display[6] = unique_segments[(5, 6)] - final_display[5]

    decoded = []
    for i in final_display:
        decoded.append(*i)
    return decoded


def decode_output(signal_patterns, output):
    signal_board = {(1, 2, 3, 5, 6, 7): "0", (3, 7): "1",
                    (2, 3, 4, 5, 6): "2", (2, 3, 4, 6, 7): "3",
                    (1, 3, 4, 7): "4", (1, 2, 4, 6, 7): "5",
                    (1, 2, 4, 5, 6, 7): "6", (2, 3, 7): "7",
                    (1, 2, 3, 4, 5, 6, 7): "8", (1, 2, 3, 4, 6, 7): "9"}
    decoded = decode_display(signal_patterns)
    final_output = []
    for number in output.strip().split():
        num = [decoded.index(c) for c in number]
        num.sort()
        final_output.append(signal_board[tuple(num)])
    return int("".join(final_output))
