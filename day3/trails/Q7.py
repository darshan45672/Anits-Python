# Write a Python program that takes a string and returns a dictionary with the count of each word in the string.

word = input("Enter a string: ")
word_list = word.split() 

word_dict = {}  

for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(word_dict)