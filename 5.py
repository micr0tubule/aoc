
with open('5') as f: 
    codes = f.readlines() 
        
def find_seat(code):
    row = 0
    for i, char in enumerate(code[:-3]): 
        if char == 'B': 
            row += 2**(6-i)
    column = 0  
    for i, char in enumerate(code[6:]): 
        if char == 'R': 
            column += 2**(3-i)
    return row, column

def id(seat_position):
    return seat_position[0]*8+seat_position[1]

answer = max([id(find_seat(code)) for code in codes]) 
# 944
