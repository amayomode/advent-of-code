from parse_input import parseInput

# Again I will just brute force this part.
# There should be an easier solution for this but this brain don't work no more


def launch_probe(init_vels, target_area):
    x_pos, y_pos = 0, 0
    xvel, yvel = init_vels
    x0, x1 = target_area[0]
    y0, y1 = target_area[1]
    while True:
        # Change the position
        x_pos += xvel
        y_pos += yvel

        # check if within target area
        if x0 <= x_pos <= x1 and y0 <= y_pos <= y1:
            return True

        # check if out of boundaries
        if x_pos > x1 or y_pos < y0:
            return False

        # update vels
        xvel -= 1 if xvel > 0 else (-1 if xvel < 0 else 0)
        yvel -= 1


def num_of_hits(target_area):
    x_max = target_area[0][1]
    y_max = -target_area[1][0]
    hits = 0
    for xvel in range(x_max + 1):
        for yvel in range(-y_max, y_max):
            if launch_probe([xvel, yvel], target_area):
                hits += 1
    return hits


if __name__ == '__main__':
    target_area = parseInput("input.txt")
    print(num_of_hits(target_area))
