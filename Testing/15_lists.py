"""
list: to store a lot of data
We can use a list to store multiple characters on screen of a game, list of items in shopping cart

DATA TYPES:
- string (short for "string of characters")
- integer
- floating point
- boolean
- lists
- tuples
- arrays

to display what type of data a value is:
print(type(3))
 -----> <class 'int'>

lists are similar to arrays
a list can be resized, but array can't

to create a list:
x = [10, 20]
print(x)
 -----> [10, 20]

print individual items in list:
print(x[0])
 -----> 10

the nr w the item's location is called the index
List locations start at zero
E.g. list / array w 10 elements doesn't have an element in spot[10]
-- just spots [0] - [9]

Don't mix the index & the value
The position (aka index) -- where a value is
The value - the actual nr stored at that location

You can also access elements from the BACK-SIDE of an array using NEGATIVE NRS
(not all langs support this)
E.g. x = [10, 20, 30]
print(x[-1])   -------> 30

You can assign new values to individual element in list:
x = [1, 2]
x[0] = 22  -----> x = [22, 2]

Making a tuple:
- created w parenthesis (rather than square brackets)
- it's not possible to change tuple once created
we can't assign an item in tuple a new value
E.g. x = (1, 2)
x[0] = 22  -----> it will cause an error

Why want this limitation?
- computer can run faster if it knows value won't change
- some lists we don't want to change ----- e.g. list of RGB colors for red

Create an empty list:
my_list = []

Iterating (Looping) Through a List
1. for each loop:
  - this type of loop takes a collection of items, & loops code once per item
  - it will take a copy of item & store it in a variable for processing

PSEUDOCODE: for item_var in list_name:
E.g.
my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)

Can store strings in lists too:
my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)

2. Use an index variable & directly access list rather than through a copy of each item
To use an index variable, the program counts from 0 up to the length of the list
If there are 10 elements, loop must go from 0-9 for a total of 10 elements

the length of a list may be found by using the len function.
combining it w range function allows code to loop through entire list

E.g.
my_list = [101, 20, 10, 50, 60]
for index in range(len(my_list)):
    print(my_list[index])

Because we're working directly w the list elements, rather than a copy, the list can be modified
for each loop doesn't allow modification of og list

Looping w Both An Index & Element:

"""
