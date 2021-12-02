with open("input.txt", "r") as f:
    horizontal = 0
    depth = 0
    aim = 0
    for line in f.readlines():
        direction, distance = line.split()
        distance = int(distance)

        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        else:
            aim -= distance

    print(horizontal * depth)
