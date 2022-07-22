import math as M
def perfect(n):
    sum=1
    i=2
    sq=int(M.sqrt(n))
    for i in range(2,sq+1):
        if(n%i==0):     
            sum=sum+i+(n/i)  
    if(sum==n):
        print("yes")
    else:
        print("no")  
n=int(input("enter a number:"))
perfect(n)     
