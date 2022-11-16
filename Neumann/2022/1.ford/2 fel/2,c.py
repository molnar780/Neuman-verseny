def has_overlap(a_start, a_end, b_start, b_end):
    latest_start = max(a_start, b_start)
    earliest_end = min(a_end, b_end)
    return latest_start <= earliest_end


with open("forgalom.txt", "r") as f:
    f=[x.split() for x in f.readlines()]
    wrong=[]
    for i in range(len(f)):
        for j in range(i, len(f)):
            #If its the same licence plate and (but) the road num is different
            if f[i][0] == f[j][0] and f[i][5] != f[j][5]:
                if has_overlap(int(f[i][1])*60 + int(f[i][2]), int(f[i][3])*60+int(f[i][4]), int(f[j][1])*60+int(f[j][2]), int(f[j][3])*60+int(f[j][4])):
                    wrong.append((f[i], f[j]))
        
for i in range(len(wrong)):
    print(wrong[i])
               
print(len(wrong))
            