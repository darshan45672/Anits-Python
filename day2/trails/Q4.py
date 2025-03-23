# given 3 sides of a triangle, determine if it is a 
# - "equilateral triangle"
# - "isosceles triangle"
# - "scalene triangle"
# - "not a triangle"


side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

if side1 !=0 and side2 !=0 and side3 !=0:
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        if side1 == side2 == side3:
            print("Equilateral Triangle")
        elif side1 == side2 or side1 == side3 or side2 == side3:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
    else:
        print("Not a Triangle")
else:
    print("Not a Triangle")