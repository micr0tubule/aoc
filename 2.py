with open('2') as f: 
    input = [line.split() for line in f.readlines()]

# part 1
count = 0
for i in input: 
    condition, letter, pw = i
    begin, end = condition.split('-')
    begin, end = int(begin), int(end)
    letter = letter[0]
    if begin <= pw.count(letter) <= end: 
        count += 1 
# 439

# part 2 
count = 0 
for i in input: 
    condition, letter, pw = i 
    pos1, pos2 = condition.split('-')
    pos1, pos2 = int(pos1), int(pos2)
    letter = letter[0]
    try: 
        if pw[pos1-1] == letter and not pw[pos2-1] == letter: 
            count += 1 
        if pw[pos2-1] == letter and not pw[pos1-1] == letter:
            count += 1 
    except IndexError as e: 
        print(pos2)
        print(pw)
        pass  
# 584


