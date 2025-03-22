# Goutam is a student at ANITS
# he has 3 internals in his 3rd year
# he has a total of 6 subjects
# to write the final sem exam he must have the average marks of 240/600
# goutam doesnt know how to calculate the average  marks
# to solve problem goutam goes near in his friend Johnny
# Johnny is ready to help goutam
# help our beloved Johnny to calculate the goutams average marks.

sub1 = int(input("Enter the marks of subject1: "))
sub2 = int(input("Enter the marks of subject2: "))
sub3 = int(input("Enter the marks of subject3: "))
sub4 = int(input("Enter the marks of subject4: "))
sub5 = int(input("Enter the marks of subject5: "))
sub6 = int(input("Enter the marks of subject6: "))
internal1 = int(input("Enter the marks of internal1: "))
internal2 = int(input("Enter the marks of internal2: "))
internal3 = int(input("Enter the marks of internal3: "))

total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + internal1 + internal2 + internal3

average = total/9

if average >= 40:
    print("Goutam is eligible to write the final exam")
else:
    print("Goutam is not eligible to write the final exam he detained")