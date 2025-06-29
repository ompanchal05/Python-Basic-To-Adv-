
# Day 005 - Lists in Python

# Creating lists
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("Middle fruits:", fruits[1:])

# List methods
fruits.append("orange")             # Adds to the end
fruits.insert(1, "grape")           # Inserts at position 1
fruits.remove("banana")             # Removes the first occurrence of 'banana'
last = fruits.pop()                 # Removes and returns the last element
fruits.sort()                       # Sorts the list alphabetically
fruits.reverse()                    # Reverses the list

print("Modified list:", fruits)
print("Popped item:", last)

# Looping through list
print("Fruits one by one:")
for fruit in fruits:
    print("-", fruit)

# List comprehension
squares = [x**2 for x in range(6)]
print("Squares:", squares)

# Practice 1: Sum of even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum([n for n in numbers if n % 2 == 0])
print("Sum of even numbers:", even_sum)

# Practice 2: Shopping list builder
shopping_list = []
while True:
    item = input("Add item (type 'done' to finish): ")
    if item.lower() == "done":
        break
    shopping_list.append(item)

print("Final Shopping List:")
for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item}")

# Practice 3: Remove duplicates
sample_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(sample_list))
print("Unique elements:", unique_list)

# Practice 4: Find max in list
print("Max number:", max(numbers))
