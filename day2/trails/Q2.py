# write a program to check if a given number is prime or not

number = int(input("Enter a number: "))

is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")