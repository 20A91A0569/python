import math as M
def prime(n):
    if(n<=1):
        return False
    s=int(M.sqrt(n))
    for i in range(2,s+1):
        if(n%i==0):
            return False
    return True
def semi(n):
    x=int(M.sqrt(n))
    for i in range(2,x+1):
        if(prime(i) and prime(n//i)):
            return True
n=int(input("enter a number:"))
r=semi(n)
print(r)
        
