def GCD(a,b):
    if b!=0:
        return GCD(b,a%b)
    else:
        return a


print("Enter 2 numbers")
x=int(input())
y=int(input())
print("HCF of these two is: ",GCD(x,y))
