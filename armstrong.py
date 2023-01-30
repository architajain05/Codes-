num=int(input("Enter any no:"))
temp=num
sum=0
i=0
while num!=0:
    i=i+1
    num=num//10
num=temp
while num!=0:
    digit=num%10
    sum=sum+digit**i
    num=num//10
if sum==temp:
    print("Armstrong no")
else:
    print("Not a armstrong no")
