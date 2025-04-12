numbers = [1, 2, 2, 3, 4, 4, 5]

#remove duplicates from the list 
unique_numbers = []

for num in numbers:
    if num not in  unique_numbers:
        unique_numbers.append(num)
    
print(unique_numbers)

print(", ".join(map(str, unique_numbers)))

#it can also be showed in other ways 

unique_numbers = list(set(numbers))
print(unique_numbers)

#other ways
seen = set()

unique_numbers1 = [num for num in numbers if not (num in seen or seen.add(num))]

print(unique_numbers1)

