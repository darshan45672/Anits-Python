# write a program that takes an integer input from the user and categorizes the number as:
# - positive even
# - positive odd
# - negative even
# - negative odd
# - zero

num = int(input("Enter a number: "))

if num == 0:
    print(f"{num} is zero")
elif num > 0:
    if num % 2 == 0:
        print(f"{num} is positive even")
    else:
        print(f"{num} is positive odd")
else:
    if num % 2 == 0:
        print(f"{num} is negative even")
    else:
        print(f"{num} is negative odd")