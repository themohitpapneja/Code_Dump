n=int(input("Enter a Number: "))
temp=n
summ=0
num=n
count=0
while(num> 0):
    num = num // 10
    count = count + 1

while n>0:
    q=n//10
    r=n%10
    n=q
    summ+=(r**count) 

if summ==temp:
    print("!!!!!!WOW!!!!!Armstrong Number!!!!!!")
else:
    print("Not an Armstrong Number")
