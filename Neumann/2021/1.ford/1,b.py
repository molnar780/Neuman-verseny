   


with open("szamok1.txt", "r") as f:
    szamok = [int(szam.strip()) for szam in f.readlines()]
    print(len(szamok)/91)
    