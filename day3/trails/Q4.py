# write a program to rotate a list k steps to the right.
# example:
# input: [1,2,3,4,5,6,7], k=3
# output: [5,6,7,1,2,3,4]

lst = [1,2,3,4,5,6,7]
k = 9

k %= len(lst)

rotated_list = lst[-k:] + lst[:-k]

print(rotated_list)