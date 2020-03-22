x=int(input())
count=0
first=0
second=1
new=0
print(0)
while(count!=x):
    count=count+1
    new=first+second
    print(new)
    first=second
    second=new

