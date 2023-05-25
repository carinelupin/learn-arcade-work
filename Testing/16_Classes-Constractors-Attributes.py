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
////////
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
