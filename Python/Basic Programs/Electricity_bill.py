##Electricity Bill Calculator, given the units consumed.
## if-else ladder
n=eval(input("Enter Units : "))
price=0
if n<=100:
    price=n*1.5+25
elif 101 <= n <= 200:
    price=(100*1.5)+(n-100)*3+50
elif 201 <= n <= 300:
    price= (100*1.5)+(100*3)+(n-200)*5+75
elif 301 <= n <= 400:
    price= (100*1.5) + (100*3) + 100 * 5 + (n - 300) * 7 + 100
else:
    price=400

print("Price is :",price)
