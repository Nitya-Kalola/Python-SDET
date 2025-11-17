# Exception handling
# Python stops execution when an error occurs unless you catch it.
# Catching this Error or handle this error called as Exception Handling.

# Example:
print(10/0)

# Basic try/except Syntax:
"""
try:
    risky_code()
except SomeError:
    handle_error()
"""

# If risky_code() throws SomeError, the except block runs.

# try/except/finally
"""
try:
    # code that may fail
except SomeError:
    # handle specific error
finally:
    # always runs
"""

"""
finally ALWAYS executes
-even if error occurs
-even if return is called
-even if break happens
-even if exception is not caught
"""

# Multiple Except Blocks
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Exception Object (as e) - captures the actual exception instance so we can access its details.

try:
    x = 1/0
except ZeroDivisionError as e:
    print(e)

# else Block - runs ONLY if no exception occurs.
# Used to separate clean flow from error flow.

try:
    x = 1/0
except ZeroDivisionError as e:
    print(e)
else:
    print("There is some issue! Please Check you code.")

