# A custom exception is simply your own exception class that inherits from Python’s built-in Exception.

"""
We create these when you want:

- clearer error messages
- consistent error types
- structured failure handling
- cleaner debugging
- framework-level control
"""

# Creating Custom Exceptions:
class LoginError(Exception):
    pass
raise LoginError("Invalid username/password")
