# While Loop - It repeats as long as a condition is True.

i = 0
while i < 5:
    print(i)
    i += 1

# Leads to Infinite Loop
i = 0
while i < 5:
    print(i)
    # forgot i += 1

# While-Else
# Just like for-loops, else executes only if the loop didn't break

i = 1
while i < 5:
    if i == 3:
        break
    i += 1
else:
    print("Loop ended normally") # It'll not run here.

# When to use While Loop :
# 1) don’t know exact iterations
# 2) waiting for something
# 3) looping until a condition becomes true
