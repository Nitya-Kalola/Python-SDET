# Dictionary - unordered, mutable, key–value mapping, hash-based (fast lookups), keys must be hashable (immutable)

# Literal syntax (most common):
user = {"name": "Nitya", "age": 21}

# Using constructor:
data = dict(name="Nitya", age=21)

# Empty dict:
d = {}

"""
Allowed keys in Dictionary:

- strings
- numbers
- tuples (if inside immutable)

Not allowed:

- lists
- sets
- dicts

Reason: keys must be immutable.
"""

# Accessing Values:
user["name"] # If key doesn’t exist it occurs KeyError.

# Safe access:
user.get("name") # returns None if missing
user.get("name", "NA") # returns "NA"

# Adding & Updating Values
# Add new:
user["email"] = "abc@gmail.com"

# Update existing:
user["age"] = 22

# Update bulk:
user.update({"role": "admin", "active": True})

# Removing Elements
# pop() - remove & return value
email = user.pop("email")

# popitem() - last inserted pair (useful for stacks)
key, value = user.popitem()

# del - Delete (no return)
del user["age"]

# clear() - Clear all elements of Dictionary.
user.clear()

# Looping Through Dictionaries:
# Keys:
user = {"Aakash":21,"Pawan":124,"Raju":234}
for k in user:
    print(k)

# Values:
for v in user.values():
    print(v)

# Key, Value pairs:
for k, v in user.items():
    print(k, v)

# Dictionary Comprehension: new = {k: v*2 for k, v in data.items()}

# Filtering: filtered = {k: v for k, v in data.items() if v is not None}

# Nested Dictionaries:
user = {
    "id": 1,
    "name": "Nitya",
    "address": {
        "city": "Pune",
        "zip": 411001
    }
}

# Access:
user["address"]["city"]

# Copy Dictionary:
# Shallow copy:
b = user.copy()
b = dict(user)

# Deep copy (for nested Dictionaries):
import copy
b = copy.deepcopy(user)

# Checking Membership:
# if "name" in user:
# Key Only, Not Value

# if "value" in user.values():
# It checks for Values of dictionary.
