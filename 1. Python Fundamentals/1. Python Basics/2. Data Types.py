# Data Type - It tells what type of data is stored in a variable.

# Every value in Python is an object.
# Each object has a type (class), value, memory location and behavior (methods).

# Major Data Types:
# 1) int - Whole numbers, Immutable E.g. 5
# 2) float - Decimal numbers, Immutable E.g. 3.14
# 3) str - Text, Immutable
# Note: 
s = "hello"
s += " world"
# This creates a new object, which is bad for heavy string operations.
# Use join() instead when handling large logs.

# 4) bool - True or False, Immutable E.g. True
# 5) list - Ordered Collection of items, Indexable, Mutable
# Example: 
a = [1,2]
b = a
b.append(3)
print(a)  # Output : [1,2,3]

# 6) tuple - Ordered Collection of items, Immutable E.g. (1,2)
# 7) dict - Collection of key-value pairs, Mutable
# Note: Always copy dicts before modifying. Use copy() method.
original = {"a": 1, "b": 2}
new_data = original.copy()

# 8) set - Unordered Collection of unique items, Mutable E.g. {1,2}

# Type Checking - isinstance(), type()
print(type(original)) # Output: <class 'dict'>
print(isinstance(original, dict)) # Output: True, Here original is an instance of dict.
