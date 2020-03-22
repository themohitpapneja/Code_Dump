## reverse a 4-digit number using operators
a=eval(input("Enter any 4-Digit Number: "))
print((),(a//1000),a%1000,a%10000)
print((a%10)*1000 + ((a//10)%100)*100 + (a%1000)*10 + (a%10000))
