# data types in python
# int,float,str,bool

a=10 #Integer
b=3.14 #Float
c="hello" #String
d=True #Boolean

# Printing the variables
print("Integer:", a)
print("Float:", b)
print("String:", c)
print("Boolean:", d)

# Type conversion (casting)

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))

# Converting int to float
a_float = float(a)
print("Converted Integer to Float:", a_float)

#converting float to int 
a_int = int(b)
print("Converted Float to Integer:", a_int)
# Converting string to int (if the string is a number)
c_int = int("123")
print("Converted String to Integer:", c_int)
# Converting string to float (if the string is a number)
c_float = float("123.45")
print("Converted String to Float:", c_float)
# Converting int to string
a_str = str(a)
print("Converted Integer to String:", a_str)
# Converting float to string
b_str = str(b)
print("Converted Float to String:", b_str)
# Converting boolean to string
d_str = str(d)
print("Converted Boolean to String:", d_str)
# Converting string to boolean (non-empty string is True)
c_bool = bool(c)
print("Converted String to Boolean:", c_bool)
# Converting integer to boolean (0 is False, non-zero is True)
a_bool = bool(a)
print("Converted Integer to Boolean:", a_bool)
# Converting float to boolean (0.0 is False, non-zero is True)
b_bool = bool(b)
print("Converted Float to Boolean:", b_bool)
# Converting boolean to integer (True is 1, False is 0)
d_int = int(d)
print("Converted Boolean to Integer:", d_int)
# Converting boolean to float (True is 1.0, False is 0.0)
d_float = float(d)
print("Converted Boolean to Float:", d_float)

# Float to int
f = 5.9
print(int(f))         

# Input and convert
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")