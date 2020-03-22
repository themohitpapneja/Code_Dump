print("**Welcome to The Hotel**")

name=input("Enter your Name: ")
ph=input("Enter Phone Number: ")
city=input("Enter your City: ")

x=int(input("Select your Stay Package\n1.Gold: 10,000Rs\n2.Silver: 7,000Rs\n3.Bronze: 4,000Rs\n"))

if x==1:
    print("**\nWelcome to Gold Package\n**")

    a = int(input("Enter No of total days stay(**ENTER 0 FOR NULL): "))
    if a==0:
        exit(0)
    else:
        print("Services Offered:\n1.Spa (500Rs/Day)\n2.Laundry (300Rs/Day)\n3.Bar 5,000Rs/Night[Unlimited Drink])"
              "\n4.Massage (2,000Rs/Person)")
        b = int(input("Enter no of days for which Spa Service is availed(**ENTER 0 FOR NULL): "))
        c = int(input("Enter no of days for which Laundry Service is availed(**ENTER 0 FOR NULL): "))
        d = int(input("Enter no of nights for which Bar Service is availed(**ENTER 0 FOR NULL): "))
        e = int(input("Enter no of persons for which Massage Service is availed(**ENTER 0 FOR NULL): "))

    bill=(a*10000) + (b*500) + (c*300) + (d*5000) + (e*2000)
    print("Name\t Phone\t City\n",name,"\t ",ph,"\t ",city)
    print("\n\nHotel Package Cost: ",a*10000)
    print("\nIndividual Cost Services\nSpa: ",(b*500),"\nLaundry: ",(c*300),"\nBar: ",(d*5000),"\nMassage: ",(e*2000))
    print("\n\nTotal Bill is: Rs",bill)

elif x==2:
    print("**\nWelcome to Silver Package\n**")
    g = int(input("Enter No of total days stay(**ENTER 0 FOR NULL): "))
    if g==0:
        exit(0)
    else:
        print("Services Offered:\n1.Lunch (250Rs/Person)\n2.Dinner (350Rs/Day)\n3.Laundry (150Rs/Day)"
          "\n4.Additional Bed (1,250Rs/Night)")
        h = int(input("Enter no of days for whom Lunch is availed(**ENTER 0 FOR NULL): "))
        k = int(input("Enter no of persons for whom Dinner is availed(**ENTER 0 FOR NULL): "))
        j = int(input("Enter no of days for which Laundry Service is availed(**ENTER 0 FOR NULL): "))
        l = int(input("Enter no of Additional beds availed(**ENTER 0 FOR NULL): "))

    bill2=(g*7000) + (h*250) + (k*350) + (j*150) + (l*1250)
    print("Name\t Phone\t City\n",name,"\t ",ph,"\t ",city)
    print("\n\nHotel Package Cost: ",(g*7000))
    print("\nIndividual Cost Services\nLunch: ",(h*250),"\nDinner: ",(k*350),"\nLaundry: ",(j*150),"\nAdditional Bed: ",(l*1250))
    print("\n\nTotal Bill is: Rs",bill2)

elif x==3:
    print("**\nWelcome to Bronze Package\n**")
    p = int(input("Enter No of total days stay(**ENTER 0 FOR NULL): "))

    if p==0:
        exit(0)
    else:
        print("Services Offered:\n1.Breakfast (100Rs/Day)\n2.Car Parking (50Rs/Car)\n3.Hot Water (50Rs/Person)")
        k = int(input("Enter no of days for which Breakfast Service is availed(**ENTER 0 FOR NULL): "))
        m = int(input("Enter no of days for which Car Parking Service is availed(**ENTER 0 FOR NULL): "))
        r = int(input("Enter no of nights for which Hot Water Service is availed(**ENTER 0 FOR NULL): "))

    bill3=(p*4000) + (k*100) + (m*50) + (r*50)
    print("Name\t Phone\t City\n",name,"\t ",ph,"\t ",city)
    print("\n\nHotel Package Cost: ",(p*4000))
    print("\nIndividual Cost Services\nBreakfast: ",(k*100),"\nCar Parking: ",(m*50),"\nHot Water: ",(r*50))
    print("\n\nTotal Bill is: Rs",bill3)

else:
    System.out.pritnln("Invalid Choice")
