with open('1') as f: 
    input = list(map(int, f.readlines()))

# part 1 
for i in input: 
    for j in input: 
        if i+j == 2020: 
            result = i*j # 1016131

# part 2 
for i in input:  
    for j in input: 
        for k in input: 
            if i+j+k == 2020: 
                result = i*j*k # 276432018