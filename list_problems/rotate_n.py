# program to rotate n elements in a list

numbers = [1, 2, 3, 4, 5, 6]

n = 2

# rotating the position from n number of spaces. we replace the first numbers and rotate the numbers from the given n position
rotate_list = numbers[-n : ] + numbers[:-n]

print(rotate_list)