# write a program to count the digits in a given number N.

N=int(input("enter the number"))
count=0

while N>0:
    count+=1
    N=N//10
print(count)