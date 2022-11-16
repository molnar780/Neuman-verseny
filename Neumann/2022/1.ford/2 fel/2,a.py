with open("forgalom.txt", "r") as f:
    f=[x.split() for x in f.readlines()]
    road_at_12 = []
    for i in range(len(f)):
        #Check if outgoing time is bigger than 12 hour in minutes and ingoing time is smaller than 12 hour in minutes
        if int(f[i][3])*60 + int(f[i][4]) >= 720 and int(f[i][1])*60 + int(f[i][2]) <= 720:
                road_at_12.append(f[i])

print(road_at_12)
print((len(road_at_12)))
            