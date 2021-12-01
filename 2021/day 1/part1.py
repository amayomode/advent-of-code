def number_increasing(depths: list[int]) -> int:
    increases = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i + 1]:
            increases += 1
    return increases


if __name__ == "__main__":
    with open("input.txt") as f:
        depths = [int(num) for num in f.readlines()]
        print(number_increasing(depths))
