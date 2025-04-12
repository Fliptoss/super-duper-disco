numbers = [1,2,3,4,5,6,7]

reverse_list = []

for i in range(len(numbers) -1, -1, -1):
    reverse_list.append(numbers[i])
    
print(reverse_list)