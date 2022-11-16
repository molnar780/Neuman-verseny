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
    last_line = calc_line_x(f, len(f))
    print(f"Az utólsó sorban a {last_line}-es szam szerepel")
    
            
            
    
    