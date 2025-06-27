# #oprators in python 
# opics Covered:
# Arithmetic Operators: +, -, *, /, //, %, **
# Comparison Operators: ==, !=, <, >, <=, >=
# Logical Operators: and, or, not
# Assignment Operators: =, +=, -=, *=, etc.
# Identity (is) and Membership (in) Operators

#Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b) # Addition
print("Subtraction:", a - b) # Subtraction
print("Multiplication:",a*b) #multiplication
print("Division:",a/b)#division
print("Floor division:",a//b) # Floor division
print("Modulus:",a%b)# Modulus
print("Exponentiation:",a**b)# Exponentiation

# Comparison Operators
print("Equal to:", a == b) # Equal to
print("Not equal to:", a != b) # Not equal to
print("Greater than:", a > b) # Greater than
print("Less than:", a < b) # Less than
print("Greater than or equal to:", a >= b) # Greater than or equal to
print("Less than or equal to:", a <= b) # Less than or equal to

# Logical Operators
x = True
y = False
print(x and y)
print(x or y)
print(not x)

#Assignment Operators
c=5
c+=2 # c = c + 2
print("After +=:", c)

# Identity and Membership
list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)      
print(2 in list1) 