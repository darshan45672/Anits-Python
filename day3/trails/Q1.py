# write a python program to reverse a given list of numbers.

n = []

N = int(input("Enter the number of elements in the list: "))

for i in range(N):
    n.append(int(input("Enter the element: ")))

print(n)
n.reverse()
print("the reversed list is: ", n)