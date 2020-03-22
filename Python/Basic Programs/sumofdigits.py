##Sum and reverse of digits of a number
n=int(input("Enter a Number: "))
summ=0
rev=0
while n>0:
    r=n%10
    n=n//10
    summ+=r
    rev=(rev*10)+r

print("Sum of digits is: ",summ)
print("Reverse of numbers is: ",rev)