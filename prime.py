import math
def prime(n):
    x=int(math.sqrt(n))
    count=0
    for i in range(2,x):
        if(n%i==0):
            count=count+1       
    if(count==0):
        print("prime")
    else:
        print("non prime")
n=int(input("enter a number"))
prime(n)

    
    
    
    
