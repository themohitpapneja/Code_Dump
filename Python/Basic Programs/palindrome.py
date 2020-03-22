n=int(input("Enter any Number: "))

rev=0
temp=n

while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r

if(temp==rev):
    print("Yes! it is a palindrome")
else:
    print("Not a palindorme")
