## print table of number


n=int(input("Enter number whose table you want to calculate:"))
r=int(input("Enter range upto which you need to print tables:"))

for i in range(1,r+1):
    print('{} x {} = {}'.format(n,i,n*i))
