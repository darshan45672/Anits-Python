# Shyam is cr of 3rd year EEE. the class advisor has given him the task of finding the 5 the topper in class.
# As a python programmer help Shayam to find the 5th topper in the class
# input: the class strength, the marks of the students
# output: the 5th topper in the class
nums=[]
num=int(input("Enter N"))
for i in range(num):
    nums.append(int(input("Enter the element:")))
nums.sort()
if(num>=5):
    print(nums[-5])
else:
    print(nums[-1])
         
        
         