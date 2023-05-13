"""
while loop is used when a program needs to loop until a particular condition occurs

use when you want to loop until something happens

don't use range w while loop, only works w for loop

E.g. printing nrs 0 - 9
# for loop
for i in range(10):
   print(i)

# while loop
i = 0
while i < 10:
    print(i)
    i += 1

if in middle of a for / while loop & code encounters a BREAK statement,
you'll immediately exit the loop

if in middle of for / while loop & code encounters a CONTINUE statement,
you'll immediately be sent back up to top of loop

"""

# EXERCISES
# simple loop that asks user want to keep looping until says no
keep_going = "yes"
while keep_going == "yes":
    keep_going = input("Do you want to continue? ")

# fixing a bug (count down from 10)
i = 10
while i >= 0:
    print(i)
    i -= 1

# bug fix (count to 10)
i = 1
while i < 11:
    print(i)
    i += 1
