with open('4') as f: 
    input = f.read()

REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = input.split('\n\n')
valid_count = 0

# part 1 
for passport in passports:
    valid = True
    for key in REQUIRED_KEYS: 
        if key not in passport: 
            valid = False
    valid_count += 1 if valid else 0 
# 219

# part 2 
from functools import reduce
from collections import defaultdict
valid_count = 0
conditions = defaultdict(lambda: lambda x: True, **{ 
    'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    'hgt': lambda x: (x[-2:] == 'cm'and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76), 
    'hcl': lambda x: x[0] == '#' and len(x) == 7 and reduce(lambda x, y: int(x)*int(y), map(lambda x: x in '0123456789abcdef', x[1:])), 
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: len(x) == 9
}) 
# who needs regex 
for passport in passports:
    valid = True
    for key in conditions.keys(): 
        if key not in passport and key != 'cid': 
            valid = False
    passport = [i for j in passport.split(':') for i in j.split()] 
    for i in range(0, len(passport), 2): 
        key = passport[i]
        value = passport[i+1]
        if not conditions[key](value): 
            valid = False 
    valid_count += 1 if valid else 0 
# 127


    

