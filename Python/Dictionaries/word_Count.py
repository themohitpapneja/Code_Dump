##counting a character using dictionary
##convert a dictionary to a string and then print the number of occurences
d=dict()
def count(word):
      for i in word:
            d[i]=word.count(i)

word=input("Enter Word: ")
print("The Word is: ",word)
n=(input("Enter Alphabet whose count you need to find: "))
count(word.lower())
print(d.get(n.lower()))
print("Full dictionary is : \n",d)


