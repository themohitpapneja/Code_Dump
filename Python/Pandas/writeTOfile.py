##File2=open("D:/Users/Mohit/Desktop/Example2.txt","w")

with open("D:/Users/Mohit/Desktop/Example2.txt","w") as File2:
    File2.write("This is Line 1\n")
    File2.write("This is second line")


with open("D:/Users/Mohit/Desktop/Example2.txt","r") as File2:
    file_stuff=File2.read()
    print(file_stuff)

