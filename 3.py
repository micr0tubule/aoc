import numpy as np 

with open('3') as f: 
    area = f.readlines()

area = [list(filter(lambda x: x != '\n', [x for x in y])) for y in area]
area = np.array(area)

tree_count = 0
for x in range(len(area)):
    y = x*3%len(area[0])
    if area[x, y] == '#': 
        tree_count += 1
print(tree_count)
 


