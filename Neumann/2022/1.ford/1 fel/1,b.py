with open("szamok.txt", "r") as f:
    f=[x for x in f.read()]
    print(f)
    n_4digit = []
    for i in range(len(f)-3):
        n_4digit.append(f[i]+f[i+1]+f[i+2]+f[i+3])
        
        

print(n_4digit)
print(len(n_4digit))