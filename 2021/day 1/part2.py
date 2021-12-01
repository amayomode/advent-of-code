def create_sliding_windows(noise: list[int]) -> list[int]:
    depths = []
    for i in range(len(noise) - 2):
        window = sum(noise[i : i + 3])
        depths.append(window)
    return depths


def number_increasing(depths: list[int]) -> int:
    increases = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i + 1]:
            increases += 1
    return increases


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        noise = [int(num) for num in f.readlines()]
        depths = create_sliding_windows(noise)
        print(number_increasing(depths))
