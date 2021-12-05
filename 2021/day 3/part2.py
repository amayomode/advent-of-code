import numpy as np


def find_most_common(diagnostic_report, position):
    bit_position = diagnostic_report[:, position]
    ones = np.count_nonzero(bit_position == "1")
    zeros = diagnostic_report.shape[0] - ones
    if ones >= zeros:
        return "01"
    else:
        return "10"


def find_rating(diagnostic_report, rating):
    rows, cols = diagnostic_report.shape
    for i in range(cols):
        most_common_bit = find_most_common(diagnostic_report, i)[rating]
        diagnostic_report = diagnostic_report[
            diagnostic_report[:, i] == most_common_bit
        ]
        if len(diagnostic_report) == 1:
            break
    return "".join(diagnostic_report[0])


def life_support_rating(diagnostic_report):
    oxygen_rating = find_rating(diagnostic_report, 1)
    carbon_rating = find_rating(diagnostic_report, 0)
    return int(oxygen_rating, 2) * int(carbon_rating, 2)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        diagnostic_report = []
        for line in f.readlines():
            diagnostic_report.append(list(line.strip()))
        diagnostic_report = np.array(diagnostic_report)
        print(life_support_rating(diagnostic_report))
