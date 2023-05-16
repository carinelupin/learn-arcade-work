"""
have to import a code lib to create random nrs

# at top of program:
import random

don't create a file w same name as what is being imported
it will cause python to import that file instead of system library

# RANDRANGE function - creates random nrs
# random nrs 0 - 49:
my_nr = random.randrange(50)

# random nrs 100 - 200
# 2nd parameter specifies an upper-bound - not inclusive
my_nr = random.randrange(100, 201)

# RANDOM function - use if you want floating point nr
# random nrs 0 - 1
my_nr = random.random()

# random nrs 10 - 15
my_nr = random.random() * 5 + 10
"""
