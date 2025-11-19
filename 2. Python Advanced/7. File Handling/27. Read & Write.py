# with open() - Used to open a file for reading or writing.
# It Automatically closes the file - even if errors occur!

# Syntax:
"""
with open("filename.file_extension", "mode") as file:
    # Work with file
    data = file.read()
# File automatically closes here
"""

"""
Modes:
"r"	- read (error if file missing)
"w"	- write (overwrites file)
"a"	- append (adds to end)
"b"	- binary mode
"r+" - read + write
"w+" - write + read (overwrites)
"a+" - append + read
"""

with open("file.txt", "r") as f:
    print(f.read())
# with guarantees: auto close, safe cleanup, fewer bugs and no dangling file handles

with open("file.txt", "w") as f:
    f.write("Hello World")

with open("file.txt", "a") as f:
    f.write("Namaskar")

with open("img.jpg", "rb") as f: # rb - read binary
    data = f.read()

# Ways of reading files:
# 1) Read entire file
content = f.read()

# 2) Read line by line - Efficient and best for big files.
for line in f:
    print(line)

# 3) Read all lines into list
lines = f.readlines()

# 4) Read fixed number of characters
chunk = f.read(100)   # read 100 chars
# Useful when parsing logs in chunks.

# Writing files (Rules):
# Use write()
f.write("Hello\n")

# Always end log lines with newline
f.write("Starting test...\n")
# Without \n, logs become unreadable.

# Write binary files
with open("output.bin", "wb") as f:
    f.write(data)


# File pointer(cursor) moves as we read.
f.read()   # pointer at end
f.read()   # returns '' (empty)

# Reset pointer:
f.seek(0) # reset pointer at the index 0

# Checking If File Exists:
# Use os.path (never assume file is present):

import os
if os.path.exists("report.txt"):
    pass # Code here
# If file is missing, we get FileNotFoundError

# Write + Read File Together:
# 1) r+ (read + write, no overwrite):
with open("file.txt", "r+") as f:
    text = f.read()
    f.write("\nnew data")

# 2) w+ (write + read, overwrites file)
with open("file.txt", "w+") as f:
    f.write("reset") # overwrites
    f.seek(0) # reset pointer to index 0
    print(f.read()) # Output: reset

# 3) a+ (append + read)
with open("file.txt", "a+") as f:
    f.write("\nnew data") # appends(add at the end)
    f.seek(0)
    print(f.read())

# Safest Pattern for Writing Logs (SDET Standard)
with open("test.log", "a", encoding="utf-8") as f: # Text files are stored as bytes. Encoding tells Python how to convert bytes to text. UTF-8 handles all languages and emojis.
    f.write(f"[{time}] {message}\n")

# Always: append, timestamp and newline

# Exception-Safe File Operations
try:
    with open("config.json", "r") as f:
        print(f.read())
except FileNotFoundError:
    raise Exception("File not found")
# Never trust file handling - write it in try/except.

"""
Avoid this Mistakes:
- Forgetting with open() -> file leaks
- Using wrong modes (writing when expecting reading)
- Using read() on large files -> memory overload
- Not checking file existence
- Storing test credentials inside files (never do this)
- Forgetting newline in logs
- Not using binary mode for images
"""
