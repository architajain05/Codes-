ctr=0
num=int(input("Enter any number:"))
for i in range(2,num):
  if num%i==0:
  ctr=ctr+1
  break
 if ctr==0:
  print("Prime Number")
 else:
  print("Not a prime number")
  
