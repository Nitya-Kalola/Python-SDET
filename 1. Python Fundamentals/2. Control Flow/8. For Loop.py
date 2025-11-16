# For Loop - Used to iterate over a sequence (list, tuple, string, range) or other iterable objects.

# Syntax:
"""
for item in sequence:
     code to be repeated
"""

# List
for x in [10, 20, 30]:
    print(x)

# String
for ch in "Nitya":
    print(ch)

# Tuple
for x in (1, 2, 3):
    print(x)

# Set (unordered)
for x in {1, 2, 3}:
    print(x)

my_dict = {1:"Hello", 2:"World"}

# Dictionary (keys)
for key in my_dict:
    print(key)

# Dictionary (values)
for val in my_dict.values():
    print(val)

# Dictionary (Items (key + value))
for k, v in my_dict.items():
    print(k, v)

# Using range():
# range(start, stop, step)

for i in range(5):  # 0 to 4
    print(i)

for i in range(2, 10, 2):  # 2,4,6,8
    print(i)

# Looping with Index:
arr = [12312,1231,24,125,3,5]
for index, value in enumerate(arr):
    print(index, value)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# Nested Loops(Use When Necessary But Minimize):
for row in matrix:
    for col in row:
        print(col)

nums = [1,3,4,5,2]
target = 8
# For-Else:
for x in nums:
    if x == target:
        print("Found!")
        break
else:
    print("Not found")
# The else block runs only if the loop completed normally (without hitting a break). If break is executed, the else block is skipped.

# When to use For Loop :
# 1) know how many times to repeat
# 2) iterating over a list/dict/string/JSON