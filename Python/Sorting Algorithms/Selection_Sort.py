l=[]
z=[]

def selection_sort(l):
    for i in range(0,5):
        MIN=min(l)
        z.append(MIN)
        l.remove(MIN)
    return z


print("Enter Integer list of 5 values")

for i in range(0, 5):
    x = int(input())
    l.append(x)

print("List is: ",l)
print("Sorted list is: ",selection_sort(l))
