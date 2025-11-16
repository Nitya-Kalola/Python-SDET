# Input - The input() function allows us to take input from the user.

# input() always returns a string

x = input("Enter: ")
print(type(x))  # str

# int() converts a string to an integer
x = int(input("Enter: "))
print(x)  # int

# float() converts a string to a float
x = float(input("Enter: "))
print(x)  # float

# bool() converts a string to a boolean
x = bool(input("Enter: "))
print(x)  # bool

# list() converts a string to a list
x = list(input("Enter: "))
print(x)  # list

# tuple() converts a string to a tuple
x = tuple(input("Enter: "))
print(x)  # tuple

# Output - The print() function is used to output text to the screen.

# Multiple ways to print:
print("Hello")
print("A", "B", "C")  # default separator: space
print("A", "B", sep="-")  # A-B

# Print without newline:
print("Hello", end="")
print("World")

# String Formatting
# Avoid string concatenation

# 1) f-strings
name = "John"
age = 30
print(f"Hello, {name}. You are {age} years old.")

# 2) format()
name = "John"
age = 30
print("Hello, {}. You are {} years old.".format(name, age))

# 3) % formatting
name = "Bob"
age = 25
print("Hello %s, you are %d years old" % (name, age))
# Output: Hello Bob, you are 25 years old

# Escape Sequences
# \n - new line
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote

