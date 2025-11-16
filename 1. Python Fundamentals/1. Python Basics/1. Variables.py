# Variable - A reference (pointer) to an object stored in memory.

#------------------------------------------------------------------------------------------------------

a = 10
b = a
# Both a and b point to the same integer object 10.

#------------------------------------------------------------------------------------------------------

# How it stores the Value in Variable:
# => when we write a = 10, so a is placed in Stack and 10(Integer Object) is created in Heap.

#------------------------------------------------------------------------------------------------------

# Naming Rules:
# 1) Must start with letter or underscore (_)
# 2) Can contain letters, digits, underscore
# 3) Case-sensitive (value is not Equal to Value)

#------------------------------------------------------------------------------------------------------

# Other Rules:
# Rule 1: Names must be meaningful.

# Bad:
a = 10
b = "Success"

# Good:
retry_count = 10
login_status = "Success"

# Rule 2: Types are dynamic.
# No need to declare it's Type. It Dynamically Consider it's Type of Data.

const = 5 # int - Integer
const = "Five" # str - String

# Rule 3: Constants should be UPPERCASE.

BASE_URL = "https://xyz.com"
TIMEOUT = 20

# Rule 4: Avoid global variables unless absolutely needed.

# Rule 5: Don’t reuse variable names.

# Rule 6: Don’t modify mutable objects without intention.

#------------------------------------------------------------------------------------------------------

# Mutable vs Immutable Variables

# 1) Immutable (can’t change value):
"""int
float
str
tuple
bool"""

# When we change an immutable variable, we're really creating a new object.

# Example: 
x = "abc"
x += "d"
# "abcd" is New Object.

# 2) Mutable (changes in-place):
"""list
dict
set"""

# Example:
a = [1, 2, 3]
b = a
b.append(4)
print(a)   # Output: [1, 2, 3, 4]
# Here we make change in b but a is also get changed, so new object is not created, but a and b is pointing to one Object.

#------------------------------------------------------------------------------------------------------

# Multiple Assignments:
a, b, c, = 1, 2, 3

# Note: Don't do like this:
a = b = c = [] # as it all references to the Same List Object, Once we make change in a or b it also changes the value of c.
# It only works for Mutable Variables, not on Immutable Variables.

#------------------------------------------------------------------------------------------------------

# Variable Scope:
# 1) Local - Inside a function
# 2) Global - Defined outside a function
# 3) Enclosed - Nested functions
# Example of Enclosed Variable: 
def outer():
    message = "Hello"  # <- This is an ENCLOSED variable
    
    def inner():
        print(message)  # <- inner() "encloses" the 'message' variable
    
    return inner

my_func = outer()
my_func()  # Prints "Hello"

# 4) Built-in - Python keywords, functions

# Example:
timeout = 5 # Global Variable

def test_case():
    timeout = 10  # Local Variable
    # This doesn't change the global timeout
    # It's Called Variable Shadowing - variable in a local scope has the same name as a variable in an outer scope.

