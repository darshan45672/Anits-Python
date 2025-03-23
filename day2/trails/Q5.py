# write a program that takes a percentage and assigns a grade based on the following condition
# 90-100 = A
# 80-89 = B
# 70-79 = C
# 60-69 = D
# 0-59 = F

num = int(input("enter the percentage: "))

if num >= 90 and num <= 100:
    print("A")
elif num >= 80 and num <= 89:
    print("B")
elif num >= 70 and num <= 79:
    print("C")
elif num >= 60 and num <= 69:
    print("D")
else:
    print("F")
