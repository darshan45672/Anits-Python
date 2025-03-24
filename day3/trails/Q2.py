# write a program to find the 2nd largesr number int the list of numbers.

n = []

n = [int(x) for x in input("Enter the list of numbers: ").split()]
n.sort()
print("The 2nd largest number is: ", n[-2])