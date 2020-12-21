from math import prod
from functools import partial
from part1 import count_trees


slopes = [
    (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
]


multiple_trees = partial(count_trees, 'input.txt')
ans = prod(map(multiple_trees, slopes))
print('part2 =', ans)
