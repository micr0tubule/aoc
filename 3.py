import numpy as np 

tree = '#'

with open('3') as f: 
    area = f.readlines()
area = [list(filter(lambda x: x != '\n', [x for x in y])) for y in area]
area = np.array(area)

# part 1 
tree_count = 0
for i in range(area.shape[0]):
    x = i*3%area.shape[1]
    y = i
    if area[y, x] == tree: 
        tree_count += 1

# part 2  
def encountered_trees(area: np.array, slope: tuple) -> list:
    tree_count = 0 
    for i in range(area.shape[0]): 
        x = i*slope[0]%area.shape[1]
        y = i*slope[1]
        if y > area.shape[0]: 
            break
        if area[y, x] == tree: 
            tree_count += 1
    return tree_count

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

from functools import reduce 
from operator import mul 

reduce(mul, [encountered_trees(area, slope) for slope in slopes]) # 2698900776

 