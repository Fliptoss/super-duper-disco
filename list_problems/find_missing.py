# we are required to find the missing numbers from a given sequence 

numbers = [1,2,3,5,6,9]

missing_num = [num for num in range(min(numbers), max(numbers) + 1) if num not in numbers]

# new_list = numbers + missing_num
# new_list.sort() #by using the sort function, it take O(nlogn)

# we can reduce the time complexity to O(n)

def merge_sort(list1, list2):
    merge_sort = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_sort.append(list1[i])
            i += 1
        else:
            merge_sort.append(list2[j])
            j += 1
    
    merge_sort.extend(list1[i:])
    merge_sort.extend(list2[j:])
    
    return merge_sort

new_list = merge_sort(numbers, missing_num)

print(new_list)

