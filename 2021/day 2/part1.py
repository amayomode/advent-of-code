with open("input.txt", "r") as f:
    horizontal = 0
    depth = 0
    for line in f.readlines():
        direction, distance = line.split()
        distance = int(distance)

        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        else:
            depth -= distance

    print(horizontal * depth)
