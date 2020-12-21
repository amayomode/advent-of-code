def count_trees(fname, slope):
    x, y = 0, 0
    count = 0
    file = open(fname, 'r')
    items = file.readlines()
    while y < len(items)-1:
        x += slope[0]
        y += slope[1]
        pattern = items[y]
        l = len(pattern.strip())
        if pattern[x % l] == '#':
            count += 1
    file.close()
    return count


ans = count_trees('input.txt', (3, 1),)

print('part1 =', ans)
