# Operators - Used to perform operations on variables and values.

# 1) Arithmetic Operators
# 2) Assignment Operators
# 3) Comparison Operators
# 4) Logical Operators
# 5) Identity Operators
# 6) Membership Operators
# 7) Bitwise Operators

# 1) Arithmetic Operators
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a // b)  # Output: 3
print(-5//2)  # Output: -3, floor goes towards negative infinity
print(a % b)  # Output: 1
print(-5 % 2)  # Output: 1
print(a ** b)  # Output: 1000

# 2) Assignment Operators
a = 10
a += 5  # a = a + 5
print(a)  # Output: 15
a -= 5  # a = a - 5
a *= 5  # a = a * 5
a /= 5  # a = a / 5
a %= 5  # a = a % 5
a **= 5  # a = a ** 5
a //= 5  # a = a // 5

# 3) Comparison Operators
a = 10
b = 3
print(a > b)  # Output: True
print(a < b)  # Output: False
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a >= b)  # Output: True
print(a <= b)  # Output: False

# 4) Logical Operators
a = True
b = False
print(a and b)  # Output: False
print(a or b)  # Output: True
print(not a)  # Output: False

# 5) Identity Operators
a = None
b = 10
print(a is None)  # Output: True
print(a is not b)  # Output: True
# Used only for: None, booleans, object identity checks
# Note: Not use Identity Operators for Numbers, cause it only gives correct answer from -5 to 256 as it only caches it till this range.

# 6) Membership Operators
a = [1,2,3]
print(1 in a)  # Output: True
print(4 not in a)  # Output: True
print("an" in "banana")  # True, because "in" on strings checks substring, not full words

# 7) Bitwise Operators
a = 10
b = 3
print(a & b)  # Output: 2
print(a | b)  # Output: 11
print(a ^ b)  # Output: 9
print(~a)  # Output: -11
print(a << 2)  # Output: 40
print(a >> 2)  # Output: 2

# 8) Ternary Operator
a = 10
b = 3
print("a is greater") if a > b else print("b is greater")

# 9) Operator Precedence

"""
**
+ - ~
* / // %
+ -
<< >>
&
^
|
comparison operators -> (< > <= >=, etc.)
== !=
not
and
or
"""