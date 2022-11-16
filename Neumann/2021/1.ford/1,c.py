   


with open("szamok1.txt", "r") as f:
    szamok = [int(szam.strip()) for szam in f.readlines()]
    ossz=0
    for i in range(len(szamok)):
        if i % 2 == 0:
            ossz+=szamok[i]
        else:
            ossz-=szamok[i]
    