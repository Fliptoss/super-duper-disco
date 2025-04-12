# Write a program to find the longest increasing subsequence in a list of numbers.

# so we need to find the sequence of the numbers where the previous one or the next one is bigger than the other one
# in order for us to find, we need to address the numbers in the list

# we can take two loop, one for the first num and second num and compare each other
# if the current is greater than the previous, we update the sequence 

# def longest_increasing_sequence(nums):
#     n = len(nums)
#     lis = [1] * n
    
#     for i in range(1, n):
#         for j in range(i):
#             if nums[i] > nums[j] and lis[i] < lis[j] + 1:
#                 lis[i] = lis[j] + 1
        
#     return max(lis)

# print("Length of Longest Increasing Subsequence:", longest_increasing_sequence(numbers))

# if we want to see the numbers that has been selected, we can do this way
def longest_increasing_sequence(nums):
    n = len(nums)
    lis = [1] * n
    parent = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                parent[i] = j
                
    #find the index of the max lis 
    max_length = max(lis)
    max_index = lis.index(max_length)
    
    #putting the values in a list
    lis_seq = []
    while max_index != -1:
        lis_seq.append(nums[max_index])
        max_index = parent[max_index]
        
    return max_length, lis_seq


numbers = [10, 22, 9, 33, 21, 50, 41, 60]

length, sequence = longest_increasing_sequence(numbers)
print("Length of Longest Increasing Subsequence:", length)
print("Longest Increasing Subsequence:", sequence)