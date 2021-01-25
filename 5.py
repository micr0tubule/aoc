with open('5') as f:
    codes = f.readlines()

def find_seat(code):  
    code = code.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0').strip('\n')
    return int(code[:7], 2), int(code[-3:], 2)

def id(seat_position):
    return seat_position[0]*8+seat_position[1]

seat_ids = [id(find_seat(code)) for code in codes]
     
# part 1   
answer = max(seat_ids) 
# 944

# part 2 
seat_ids = sorted(seat_ids)
answer = max(set(range(seat_ids[0], seat_ids[-1])) - set(seat_ids))
# 554



# def find_seat(code):
#     row = 127
#     for i, char in enumerate(code[:-4]): 
#         if int(char): 
#             row -= 2**(6-i)
#     column = 0  
#     for i, char in enumerate(code[6:]): 
#         if char == 'R': 
#             column += 2**(3-i)
#     return row, column