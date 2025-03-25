# write a function tha returns the count of unique characters in the string
# input: "hello"
# output: 4

# def uniqueCharCount(s):
#     count = {}

#     for i in s:
#         count[i] = True
#     return len(count)

# def uniqueCharCount(s):
#     count =[]
#     for i in s:
#         if i not in count:
#             count.append(i)
#     return count

# def uniqueCharCount(s):
#     count = 0
#     for i in s:
#         if i not in s[:count]:
#             count += 1
#     return count

def uniqueCharCount(s):
    return len(set(s))

string = input("Enter a string: ")

length = uniqueCharCount(string)
print(length)