

with open('2') as f:
    passwords = [password.split(':') for password in f.readlines()]

count = 0
for condition, password in passwords: 
    num, letter = condition.split()
    start, end = num.split('-')
    start, end = int(start), int(end)
    letter_count = password.count(letter)
    if start <= letter_count <= end: 
        count += 1 
print(count)

