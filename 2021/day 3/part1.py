import numpy as np


def power_consumption(diagnostic_report):
    gamma = epsilon = ""
    rows, cols = diagnostic_report.shape
    for i in range(cols):
        bit_position = diagnostic_report[:, i]
        ones = np.count_nonzero(bit_position == "1")
        zeros = rows - ones
        if ones > zeros:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        diagnostic_report = []
        for line in f.readlines():
            diagnostic_report.append(list(line.strip()))
        diagnostic_report = np.array(diagnostic_report)
        print(power_consumption(diagnostic_report))
