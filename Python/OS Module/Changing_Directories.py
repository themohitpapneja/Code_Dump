from os import *
print(getcwd())

print(listdir('D:\\Users\\Mohit\\PycharmProjects\\PythonLab\\venv'))
print("Current Directory is: ",getcwd())
k=input("Enter Directory Where you want to jump: ")
print("Changing Directory.......")
chdir(k)
print("Current Directory is: ",getcwd())
print("Listing )the directories in current directory....\n",listdir(k))