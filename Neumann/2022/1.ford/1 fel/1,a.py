with open("szamok.txt", "r") as f:
    f=[int(x) for x in f.read()]
    print(f)
    num_of_0 = 0
    for i in f:
        if i == 0:
            num_of_0+=1

print(num_of_0)