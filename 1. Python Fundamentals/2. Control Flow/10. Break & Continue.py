# Break - immediately stops the loop (for or while).

for x in [1,2,3,4]:
    if x == 3:
        break
    print(x,end = " ") # Output: 1 2

for i in range(5):
    if i == 3:
        break
        print("never runs") # This will never run, because the loop is broken.
    print(i)


# break inside nested loops only breaks the inner loop, not all loops.

for x in [1,2,3,4]:
    for y in [1,2,3,4]:
        if y == 3:
            break
        print(y,end = " ") # Output: 1 2 1 2 1 2 1 2

# Continue - skips the current iteration of the loop (for or while).

for x in [1,2,3,4]:
    if x == 3:
        continue
    print(x,end = " ") # Output: 1 2 4

# This may leads to error, because it will skip the loop and not increment the value of i.
i = 0
while i < 5:
    if i == 2:
        continue
    i += 1
    print(i)