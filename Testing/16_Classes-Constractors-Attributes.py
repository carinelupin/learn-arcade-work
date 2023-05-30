"""
object-oriented programming:
- group multiple vars together in single record
- associate functions w group of data
- use inheritance -- allows us to take base set of code & extend it, w/out needing to rewrite it from scratch

##### Classes
//////// DEFINING CLASSES
- Each data item grouped into class is called: a field, attribute / instance variable
- Class names starts w capital letter

\\Text from comments can be pulled out automatically to form a website for your API documentation

//////// DEFINING INT FUNCTION

- when create new instance of class,
we need code that'll create our attributes (vars) & set them to default vals
i.e. __init__ method

- any function in a class -- called a "method"
- the initialization (first) method is called automatically
- methods invoked automatically also called a "magic method" & also "dunder methods"
- "magic method" names are surrounded w double underscores - (2 back, 2 front)
- 2 underscores -- also called a "dunder"
- all methods in a class have at least 1 parameter & 1st parameter is always self

//////// DEFINING CLASS ATTRIBUTES
- like functions, variables created in methods are forgotten after method is done running,
- if you want to keep it, return as value

- the "self" parameter refers to memory associated w each instance of the class
- use "self" to create vars that keep value for as long as object exists
- attributes, fields, instance variable --- variables that exist as part of a class
- attributes must be set to a default value
- that value is often 0, an empty string, or special value "None"

- if not put "self" in front of vars, computer would forget vars once __init__ func was done

- the __init__ is a special method that may be referred to as a "constructor"
- in other langs, term "constructor" is generic term used to refer to that lang equivalent to __init__ method

- the "self" is like pronoun "my"
- inside class we talk about my var --- e.g. my name, my city, my car, etc.
- don't use self outside class
- bc like "my" it means someone different if said by different person

##### Objects
//////// CREATING OBJECTS
- class code defines a class but doesn't actually create an instance of one
- code told computer what fields address has but don't have address yet
- we can define a class w/out creating one
 E.g.
 def main():
    #create address
    home_address = Address()

We need a variable that will point to our address.   E.g. home_address.
We’ll set that variable equal to the new instance of the class we create.
We create a new instance by using the name of the class (Address), followed by parentheses.
This will “magically” call the __init__ method which will set up fields/attributes for the class.

In this case, Address is a class. It defines what an address looks like.
The home_address variable points to an object.
An object is an instance of a class. It is the actual address.
As another example, “Human” is a class, while “Samantha” and “Pete” are instances of the class.

You can set the object’s attributes using the dot operator.
First, use the variable that points to our object,
   immediately follow that with a period, then the attribute name.

E.g.
def main():
    # Create an address
    home_address = Address()

    # Set the fields in the address
    home_address.name = "John Smith"
    home_address.line1 = "701 N. C Street"
    home_address.line2 = "Carver Science Building"
    home_address.city = "Indianola"
    home_address.state = "IA"
    home_address.zip = "50125"

A second variable can be created that points to a completely different instance of the Address class:

    # Create another address
    vacation_home_address = Address()

    # Set the fields in the address
    vacation_home_address.name = "John Smith"
    vacation_home_address.line1 = "1122 Main Street"
    vacation_home_address.line2 = ""
    vacation_home_address.city = "Panama City Beach"
    vacation_home_address.state = "FL"
    vacation_home_address.zip = "32407"

    print("The client's main home is in " + home_address.city)
    print("His vacation home is in " + vacation_home_address.city)

Attributes are not limited to being simple strings and numbers!
If you have a class that represents a graph,
   you can store all the data points in an attribute that is a list.
Attributes can even be other objects.
An object that represents a player character in an adventure could have
   an attribute with another object that represents a magical hat.

"""

# class E.g.


class Character:
    """
    represents player character
    """
    def __init__(self):
        """ setting up the vars in object """
        self.name = ""
        self.outfit = ""
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.armor_amount = 0
        self.max_speed = 0
