# write a program to print the multiplication table of a given number N.
# Output should be in the following format:
N=int(input("enter the number"))    
mul=0
if N>0:
    for i in range(1,11):
        mul=N*i
        print(N,"*",i,"=",mul)
else:
    print("enter a positive number")