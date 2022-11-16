def time_on_road(in_h, in_m, out_h, out_m):
    t_minute = (out_h*60 + out_m) - (in_h*60 + in_m)
    if t_minute > 0:
        return t_minute/60
    else:
        #past 24 hour, in minutes 
        t_minute = (1440 + out_m) - (in_h*60 + in_m)
        return t_minute/60

with open("forgalom.txt", "r") as f:
    f=[x.split() for x in f.readlines()]
    over_100km_per_h = [] 
    for i in range(len(f)):
        #The time of the car while on the road in minutes
        t_hour = time_on_road(int(f[i][1]), int(f[i][2]), int(f[i][3]), int(f[i][4]))
        #the speed of the car on a 10 km road in hours now
        v=10/t_hour
        if v >= 100:
            over_100km_per_h.append(f[i])
        
print(over_100km_per_h)
print((len(over_100km_per_h)))
            