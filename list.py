# fruits = ["apple","banana","cherry"]
# fruits.append("coco") # Adding an item
# # print(fruits[2]) # Output: apple
# print(len(fruits))
# print(fruits[3])

# Slicing data
# numbers = [1, 2, 3, 4, 5]
# print(numbers[1:3]) # Output: [2, 3, 4]


# List Comprehension
# squares = [x**2 for x in range(5)]
# print(squares) # Output: [0, 1, 4, 9, 16]

# Sorting and Reversing
# numbers = [5, 2, 9, 1]
# numbers.sort() # Sorting the list in ascending order
# print(numbers) # Output: [1, 2, 5, 9]
# numbers.reverse() # Reversing the list
# print(numbers) # Output: [9, 5, 2, 1]


v1 = [8,6,4,12,1]
v2 = [2,7,13,16,19]
v3 = [18,10,3,5,9]
v4 = [20,11,14,17,15]


gbg1 = sorted(v1 + v2) 
gbg2 = sorted(v3 + v4)
hasil1 = sorted(gbg1 + gbg2)
print(hasil1)