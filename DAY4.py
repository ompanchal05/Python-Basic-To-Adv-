# Creating strings
greeting = "Hello"
name = "Om"

# Concatenation
message = greeting + " " + name
print(message)  

# Repetition
print("Ha" * 3)  

# Indexing
print(name[0])   
print(name[-1])  

# Slicing
print(name[0:2]) 
print(name[::-1]) 

# String Methods
s = "   Hello World!   "
print(s.lower())     
print(s.strip())      
print(s.replace("World", "Om"))  

# Escape Characters
quote = "She said, \"Python is fun!\""
print(quote)

# String Formatting
age = 20
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

# Multiline Strings
multiline_string = """This is a string
that spans multiple lines."""
print(multiline_string)