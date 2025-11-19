# JSON - JavaScript Object Notation, is a lightweight, text-based format for storing and exchanging data that is both human-readable and machine-parsable.
# JSON is often used for storing and transporting data between a server and a web application.

# Reading JSON File - json.load()
import json

with open("file.json") as f:
    data = json.load(f)
    print(data)
# JSON file may contain either JSON Object or JSON Array.
# JSON Object in python consider as Dictionary.
# JSON Array in python consider as List.

# Writing JSON File - json.dump()
with open("dummy.json", "w") as f:
    json.dump(data, f, indent=4) # Writes/dump data to empty dummy.json file
# indent=4 - adds indentation of 4 spaces.

# Reading JSON From a String
json_string = '{"name": "Nick", "age": 69}'
data = json.loads(json_string)
# loads() = load from string
# load() = load from file

# Writing JSON to String
json_str = json.dumps(data, indent=2)
# dumps() = dump to string
# dump() = dump to file

# JSON VS Python Types:
"""
JSON        Python

object	    dict
array	    list
string	    str
number	    int/float
true/false	True/False
null	    None
"""

# Validating JSON Structure
# Check if a field exists:
if "status" not in data:
    raise KeyError("Missing field: status")

# Validate type:
if not isinstance(data["age"], int):
    raise TypeError("Age must be integer")

# Updating JSON Data
# Add new value:
data["role"] = "admin"

# Modify value:
data["role"] = "editor"

# Remove value:
data.pop("role", None)

# Handling Nested JSON
data = {
  "user": {
    "id": 1,
    "details": {
      "city": "Pune",
      "verified": true
    }
  }
}

# Access:
data["user"]["details"]["city"] # Output: Pune

# Safe JSON Parsing
try:
    data = json.loads(json_string)
except json.JSONDecodeError:
    print("Invalid JSON")
# or
try:
    with open("file.json") as f:
        data = json.load(f)
except ValueError:
    raise Exception("Invalid JSON received")

# Forcing ASCII / Ensuring Unicode:
# By default, json.dumps() escapes non-ASCII characters
data = {"name": "José", "city": "München", "text": "北京"}

print(json.dumps(data)) # Output : {"name": "Jos\u00e9", "city": "M\u00fcnchen", "text": "\u5317\u4eac"}
# Escapes non-ASCII characters
# In this ensure_ascii=True is By default

# Preserve actual characters
print(json.dumps(data, ensure_ascii=False)) # Handling Non-English Characters
# Output : {"name": "José", "city": "München", "text": "北京"}

# Sorting Keys
print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4))
# Output : {"city": "München", "name": "José", "text": "北京"}
