n=int(input("enter the value"))
if n>2:
   for i in range (2,n):
       if (i%n)==0:
           print(n,"is not prime")
           break
   else:
           print(n,"is prime")