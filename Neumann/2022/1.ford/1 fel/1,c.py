def is_prime(num):
    if num > 1:
    # check for factors
        for i in range(2, round(num//2)+1):
            if num % i == 0:
                return False
        return True
       
    

with open("szamok.txt", "r") as f:
    f=[x for x in f.read()]
    print(f)
    n_4digit = []
    for i in range(len(f)-3):
        #Joins together four nums from the list, and converts to int n 
        n=int(f[i]+f[i+1]+f[i+2]+f[i+3]) 
        if is_prime(n):
            n_4digit.append(n)
        
        

print(n_4digit)
print(len(n_4digit))