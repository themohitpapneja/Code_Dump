## Greatest of three numbers using nested if-else.
a=float(input("Enter A : "))
b=float(input("Enter B : "))
c=float(input("Enter C : "))

if a>b:
    if a>c:
        print("A is largest")
    else:
        print("C is largest")
else:
    if b>c:
        print("B is largest")
    else:
        print("C is largest")
