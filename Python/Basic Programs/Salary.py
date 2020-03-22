##To find Salary of a person given his sales.

n=float(input("Enter Sales : "))
basic=4000.00
if n>=100000:
    print("You belong to Category 1!(Sales>=1 Lacs)")
    conv=500.00
    bonus=1000.00
    salary=basic+(0.2*basic)+(1.1*basic)+conv+(0.1*n)+bonus
    print("Your Salary: ",salary)
elif 0 <= n <= 100000:
    print("You belong to Category 2!(Sales<=1 Lacs)")
    conv=500.00
    bonus=500.00
    salary=basic+(0.1*basic)+(1.1*basic)+conv+(0.04*n)+bonus
    print("Your Salary: ",salary)
else:
    print("Invalid Value! Salary Cannot be Negative")
