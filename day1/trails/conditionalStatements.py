# the user will give 2 cartesian points and you have to predict on which quadrant the point will lie
# The quadrants are as follows:
# 1st quadrant: x>0, y>0
# 2nd quadrant: x<0, y>0
# 3rd quadrant: x<0, y<0
# 4th quadrant: x>0, y<0
# If the point lies on the x-axis, then print "x-axis"
# If the point lies on the y-axis, then print "y-axis"
# If the point lies on the origin, then print "origin"

x = int(input("Enter the x coordinate: "))
y = int(input("Enter the y coordinate: "))

print("x = ", x)
print("y = ", y)

if x>0 and y>0:
    print("1st quadrant")
elif x>0 and y<0:
    print("4th quadrant")
elif x<0 and y>0:
    print("2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
elif x==0 and y!=0:
    print("y-axis")
elif x!=0 and y==0:
    print("x-axis")
else:
    print("origin") 