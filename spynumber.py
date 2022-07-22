from perfect import *
def spy(n):
    sum=0
    pro=1
    while(n>0):
        r=n%10
        sum=sum+r
        pro=pro*r
        n=int(n/10)
    if(sum==pro):
        print("yes")
    else:
        print("no")
n=int(input("enter a number"))
spy(n)
perfect(n)
