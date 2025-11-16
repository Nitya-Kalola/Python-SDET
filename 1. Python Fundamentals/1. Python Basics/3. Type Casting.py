# Type Casting - Creates a new object of the target type.

x = "10"
y = int(x)
# x still points to "10" (str).
# y points to a new object 10 (int).

# Types of Type Casting:

# 1) Explicit Casting (Only thing you control)
# We call constructors.
# int(), float(), str(), bool(), list(), tuple(), dict(), set()

# 2) Implicit Casting (Python does it automatically)
# Example:
print(10 + "10")  # Output: 1010
# 10 is converted to str
print(1 + 5.6)  # Output: 6.6 
# 1 is converted to float

# int() :
x = int(1)   # x will be 1
y = int(2.8) # y will be 2, It will truncate the float
z = int("3") # z will be 3
a = int("4.3") # Gives an Error, cause it's not a whole number
b = int("abc") # Gives an Error, cause it's a string

# float() :
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
a = float("4.3") # a will be 4.3
b = float("abc") # Gives an Error, cause it's a string
c = float("1e-2") # c will be 0.01

# str() :
# It works on any data type
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
l = str({"a": 1})  # l will be '{"a": 1}'

# bool() :
x = bool(1)   # x will be True
print(bool(234)) # True
y = bool(0)   # y will be False
a = bool("abc") # a will be True (non-empty string)
b = bool("")   # b will be False (empty string)
print(bool(" "))       # True (space is still a character)
print(bool("0"))       # True (string with '0' is non-empty)
print(bool()) # False (empty string)

# list() :
x = list(("apple", "banana", "cherry")) # x will be ['apple', 'banana', 'cherry']
y = list((1, 2, 3)) # y will be [1, 2, 3]
z = list({1, 2, 3}) # z will be [1, 2, 3]
print(list({1:"Hello", 2:"World"})) # Output: [1, 2]

# tuple() :
x = tuple(["apple", "banana", "cherry"]) # x will be ('apple', 'banana', 'cherry')
y = tuple((1, 2, 3)) # y will be (1, 2, 3)
z = tuple({1, 2, 3}) # z will be (1, 2, 3)
print(tuple({1:"Hello", 2:"World"})) # Output: (1, 2)

# dict() :
x = dict(name="John", age=36) # x will be {'name': 'John', 'age': 36}
y = dict({"name":"John", "age":36}) # y will be {'name': 'John', 'age': 36}
print(dict([("a", 1), ("b", 2)])) # Output: {'a': 1, 'b': 2}
print(dict(["a", "b"])) # Gives an Error


# set() :
x = set(("apple", "banana", "cherry")) # x will be {'apple', 'banana', 'cherry'}
y = set((1, 2, 3)) # y will be {1, 2, 3}
z = set({1, 2, 3}) # z will be {1, 2, 3}
print(set({1:"Hello", 2:"World"})) # Output: {1, 2}
print(set([1,2,2,3]))  # {1,2,3}

