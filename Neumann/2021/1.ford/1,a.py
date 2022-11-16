with open("szamok1.txt","r") as f:
    lista=[int(szam.strip()) for szam in f.readlines()]
    total=0
    for i in lista:
        if i == 5:
            total+=1
    print(total)