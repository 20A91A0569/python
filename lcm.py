a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))             
i=b
n=a*b
while(i<=n+1):
      if(i%a==0 and i%b==0):
            print("lcm of %d,%d is %d"%(a,b,i))
            break
      else:
           i=i+1
