# Given an integer list, find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.

nums = [-2, 1, 3, -4, 5, 22, -1, -33, -1]

max_sum = float('-inf')
current_sum = 0
start = end = 0
temp_start = 0

for i in range(len(nums)):
    if current_sum + nums[i] < nums[i]:
        current_sum = nums[i]
        temp_start = i
    else:
        current_sum += nums[i]

    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i

subarray = nums[start : end+1]

print(" the maximum sum is ", max_sum)
print("Subarray: ", subarray)