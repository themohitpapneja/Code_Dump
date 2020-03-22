def next_15_leap(var):
    count=0
    while(count!=15):
        if((var%4==0 and var%100!=0) or (var%400==0 and var%100==0)):
            print(var)
            count=count+1
            var=var+1
        else:
            var=var+1





n=int(input("Enter year "))
next_15_leap(n)
