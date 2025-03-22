# Nithin has 3 phones
# Nithin wants to check which phone is better interms of price
# he wants his friend Rambo to help him in this case
# nitin asks rambo to give a application that will give the biggest 
# phone price out of the 3 phones
# help rambo to write the code for this application

phone1 = int(input("Enter the price of phone1: "))
phone2 = int(input("Enter the price of phone2: "))
phone3 = int(input("Enter the price of phone3: "))

if phone1 > phone2:
    if phone1 > phone3:
        print("Phone1 is the best")
    else:
        print("Phone3 is the best")
else:
    if phone2 > phone1:
        if phone2 > phone3:
            print("Phone2 is the best")
        else:
            print("Phone3 is the best")