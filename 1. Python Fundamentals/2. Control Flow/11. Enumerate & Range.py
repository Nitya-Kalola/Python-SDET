# Range - It is a sequence of numbers that creates a range object when needed.
# Range is a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# It doesn’t create a list.


# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)

for i in range(5): # Excludes 5, goes till 4
    print(i)

for i in range(1, 5):
    print(i)

for i in range(1, 10, 2): # Increment by 2
    print(i)

# Enumerate (Professional Way to Loop With Index) - It iterates over a sequence and gives (index, value) at each step.

# Syntax : for index, value in enumerate(iterable):

fruits = ["apple", "banana", "cherry"]

# Example:
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry

for i, fruit in enumerate(fruits, start=1): # Starts indexing from 1.
    print(i, fruit)

# Reverse loop with range
for i in range(len(fruits)-1, -1, -1):
    print(i)

# Using reversed() function:
for item in reversed(fruits):
    print(item)