def calc_line_x(current_line, x):
    next_line=[]
    for i in range(x-1):
        for j in range(len(current_line)-1):
            next_line.append(current_line[j] + current_line[j+1])
        current_line=next_line
        next_line=[]
    return current_line
        

with open("szamok7.txt", "r") as f:
    f=[int(x) for x in f.readlines()]
    line_6 = calc_line_x(f, 6)
    print(" A hatodik sor:\n", line_6)
    not_3_digit=[]
    for i in range(len(line_6)):
        if line_6[i] < 100 or line_6[i] > 999:
            not_3_digit.append(line_6[i])
    print(len(not_3_digit))
            
            
    
    