"""
By default, print statement puts a carriage return at end of what is printed
carriage return: a character that moves the next line of output to be printed to next line
Most of the time, it's what we want, sometimes not
If you want to PRINT ON SAME LINE, we can change default character printed at end

E.g.
print("Pink", end="")
print("Octopus")
 -----> This will print:   PinkOctopus

We can also use a space instead of setting it to an empty str
E.g.
print("Pink", end=" ")
print("Octopus")
 ------> Pink Octopus

MOVING TO THE NEXT LINE
To trigger text to appear on the next line ---> use an empty print statement
E.g. print()

"""

"""
ADVANCED LOOPING PROBLEMS
# PROBLEM 1:
# print ten asterisks in a row:
for i in range(10):
    print("*", end=" ")

# PROBLEM 2:
# print 10(*), \n 5(*) \n 20(*)
for i in range(10):
    print("*", end=" ")
print()
for i in range(5):
    print("*", end=" ")
print()
for i in range(20):
    print("*", end=" ")

# PROBLEM 3:
# 2 nested for loops + 10x10 asterisk *square (WTF??)
for i in range(10):
    for j in range(10):
        print("*", end=" ")
    print()

# PROBLEM 4:
# 2 nested for loops + 5x10 asterisk rectangle
for i in range(10):
    for j in range(5):
        print("*", end=" ")
    print()

# PROBLEM 5:
# 2 nested for loops + 20x5 rectangle
for i in range(5):
    for j in range(20):
        print("*", end=" ")
    print()

# PROBLEM 6:
# print 10 lines of nrs 0-9
for row in range(10):
    for column in range(0, 10):
        print(column, end=" ")
    print()

# PROBLEM 7:
# print 10 lines of nrs 0-9 each nr on own line (0s on one line, 1s on one line, etc.)
for row in range(10):
    for column in range(0, 10):
        print(row, end=" ")
    print()

# PROBLEM 8:
for row in range(10):
    for column in range(row + 1):
        print(column, end=" ")
    print()
    
# PROBLEM 9:  (what?????  *****DO AGAIN*****)
for row in range(10):
    for column in range(row):
        print(" ", end=" ")
    for column in range(10 - row):
        print(column, end=" ")
    print()
    
for i in range(1, 10):
    for j in range (1, 10):
         # extra space
         if i * j < 10:
             print(" ", end=" ")
             
         print(i * j, end=" ")

# PROBLEM 10: (I honestly don't know what's going on anymore, *****DO AGAIN*****)
for i in range(1, 10):
    for j in range(1, 10):
        if i * j < 10:
            print("", end=" ")

        print(i * j, end=" ")
    print()
"""

# PROBLEM 11: (*****DO AGAIN*****)
# PROBLEM 12: (*****DO AGAIN*****)
# PROBLEM 13: (*****DO AGAIN*****)
