with open("D:/Users/Mohit/Desktop/Example2.txt","r") as readfile:
    with open("D:/Users/Mohit/Desktop/Example3.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)

