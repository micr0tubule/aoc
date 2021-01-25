# part 1 
with open('6') as f: 
    groups = list(map(lambda x: x.replace('\n', ''), f.read().split('\n\n'))) 

answer = sum([len(set(g)) for g in groups]) 
# 6735

# part 2
from functools import reduce 
from collections import Counter

with open('6') as f: 
    groups = list(map(lambda x: x.split('\n'), f.read().split('\n\n')))

gsum = 0
for g in groups:
    c = Counter(''.join(g))
    for k, v in c.items():
        if v == len(g):
            gsum+=1
# 3221


