# csv - It is a module that allows us to read and write comma-separated values (CSV) files.

import csv

# Reding CSV
# 1) Basic Reader (List of Lists):
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 2) DictReader - Treats each row as a dictionary using header names.

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Reading CSV into a List
with open("data.csv") as f:
    rows = list(csv.reader(f))
    print(rows)

# Writing to CSV
# 1) writer() — Write List of Lists
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["John", 25])

# 2) DictWriter - Write List of Dictionaries
with open("out.csv", "w", newline="") as f: # newline="" removes blank lines between rows
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "John", "age": 25})

# Custom Delimiter
# Not all CSVs use commas.

# Tab-separated: Used in tsv files
reader = csv.reader(f, delimiter="\t")

# Pipe-separated:
reader = csv.reader(f, delimiter="|")

# Semicolon-separated:
reader = csv.reader(f, delimiter=";")

# Skipping Header Row
with open("data.csv", "r", newline="") as f:
    reader = csv.reader(f)
    
    # Skip the header row
    next(reader)
    
    # Now processing starts from the 2nd row (first data row)
    for row in reader:
        print(row)  # This is our data, no headers

# Writing Multiple Rows
writer.writerows([
    ["John", 25],
    ["Nitya", 21]
])

# Writing Multiple Dictionaries
writer.writerows([
    {"name": "John", "age": 25},
    {"name": "Nitya", "age": 21}
])

# Handling Quoted Fields
# CSV with commas inside values: "John, Jr.",25,Pune

# Python handles this automatically, but only if we use csv module — NOT manual splitting.
