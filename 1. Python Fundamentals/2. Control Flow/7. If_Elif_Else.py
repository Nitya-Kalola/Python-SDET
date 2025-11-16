# If/Elif/Else - Controls the execution path based on boolean conditions

# Python checks conditions top to bottom, and the first True block executes — the rest are ignored.

# Syntax:
"""
if condition1:
    ...
elif condition2:
    ...
else:
    ...
"""

"""
if -> checked first
elif -> checked only if all previous conditions were False
else -> executes only if ALL conditions were false
"""

# Bad:
"""
if status == 200:
    ...
if status == 404:
    ...
if status == 500:
    ...
"""
# Python checks all three, even if the first matches.
# This slows execution and causes duplicate logic.

# Good:
"""
if status == 200:
    ...
elif status == 404:
    ...
elif status == 500:
    ...
else:
    ...
"""

# Python doesn’t just check True/False.
# These evaluate to False:
"""
0
0.0
""
[]
{}
set()
None
False
"""
# Everything else is True.

# Example:
if []:
    print("True")
else:
    print("False")  # this runs

# Boolean Operators in Conditions
# and -> stops at first False
# or -> stops at first True

# Nested If - Use Only When Necessary
# Too much nesting makes code unreadable.
"""
if condition1:
    if condition2:
        ...
    else:
        ...
else:
    ...
"""

# Bad:
"""
if a:
    if b:
        if c:
            ...
"""

# Good:
"""
if a and b and c:
    ...
"""

# Ternary Operator — Single-line If/Else
# Useful for clean assignments.
# Syntax :  x = value_if_true if condition else value_if_false

# Example:
x = 10
output = "even" if x % 2 == 0 else "odd"
print(output)
