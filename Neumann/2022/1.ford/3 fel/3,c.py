def calc_line_x(current_line, x):
    next_line=[]
    if len(current_line)-x+1 <= 0:
        raise IndexError      
    for i in range(x-1):
        for j in range(len(current_line)-1):
            next_line.append(current_line[j] + current_line[j+1])
        current_line=next_line
        next_line=[]
    return current_line
        

with open("szamok7.txt", "r") as f:
    f=[int(x) for x in f.readlines()]
    i_said_bigger_than_1_5 = 0
    for i in range(1, len(f)-1):
        row_a = calc_line_x(f, i)
        row_b = calc_line_x(f, i+1)
        if sum(row_b)/sum(row_a) > 1.5:
            i_said_bigger_than_1_5 += 1
        
    print(i_said_bigger_than_1_5)
    
            
            
    
    