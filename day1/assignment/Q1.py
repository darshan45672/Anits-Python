# Abhinaya is a student at ANITS
# She is a very good student and she is very much interested in programming
# She is learning python and she is very much interested in solving problems
# She is given a task to solve
# the task is as follows:
# bhuvana is her best friend
# bhuvana is a student at ANITS
# bhuvana gives 3 inputs to Abhinaya
# The inputs are x, y and z which are the angles of a triangle
# Abhinaya has to find the wether the given angles are of a triangle or not
x=int(input("enter the first angle"))
y=int(input("enter the second angle"))
z=int(input("enter the third angle"))
if x+y+z==180 and x!=0 and y!=0 and z!=0 and x!=90 and y!=90 and z!=90 and x!=180 and y!=180 and z!=180:
    print("The given angles are of a triangle")
else:
    print("The given angles are not of a triangle")