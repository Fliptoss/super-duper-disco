# we are to merge two list in sorted order 
# we need to make sure that the remaining elements are also added to the list

list1 = [1,3,5,7,9]
list2 = [2,4,6]

merge_list = []
i, j = 0, 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merge_list.append(list1[i])
        i += 1
    elif list1[i] > list2[j]:
        merge_list.append(list2[j])
        j += 1

# we take the rest of the elements and add them to the list      
merge_list.extend(list1[i: ])
merge_list.extend(list2[j: ])

print(merge_list)