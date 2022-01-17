from parse_input import parseInput

# I did not have time so brute force will do


def launch_probe(init_vels, target_area):
    x_pos, y_pos = 0, 0
    xvel, yvel = init_vels
    x0, x1 = target_area[0]
    y0, y1 = target_area[1]
    # track max height
    max_height = -float('inf')
    while True:
        # Change the position
        x_pos += xvel
        y_pos += yvel

        # check if new max_height found
        if y_pos > max_height:
            max_height = y_pos

        # check if within target area
        if x0 <= x_pos <= x1 and y0 <= y_pos <= y1:
            return max_height

        # check if out of boundaries
        if x_pos > x1 or y_pos < y0:
            return 0

        # update vels
        xvel -= 1 if xvel > 0 else (-1 if xvel < 0 else 0)
        yvel -= 1


def max_height(target_area):
    x_max = target_area[0][1]
    y_max = -target_area[1][0]
    max_height = -float("inf")
    for xvel in range(x_max + 1):
        for yvel in range(-y_max, y_max):
            height = launch_probe([xvel, yvel], target_area)
            if height > max_height:
                max_height = height
    return max_height


if __name__ == '__main__':
    target_area = parseInput("input.txt")
    print(max_height(target_area))
