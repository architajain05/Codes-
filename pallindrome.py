num=int(input("Enter any no:"))
temp=num
sum=0
while num!=0:
    digit=num%10
    sum=sum*10+digit
    num=num//10
if temp==sum:
    print("Pallindrome Number")
else:
    print("Not a Pallindrome Number")
