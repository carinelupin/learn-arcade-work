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

- any function in a class -- called a method
- the initialization (first) method is called automatically
- methods invoked automatically also called a "magic method" & also "dunder methods"
- "magic method" names are surrounded w double underscores - (2 back, 2 front)
- 2 underscores -- also called a dunder
- all methods in a class have at least 1 parameter & 1st parameter is always self

//////// DEFINING CLASS ATTRIBUTES
- if not put "self" in front of vars, computer would forget vars once init func was done


class E.g.


"""


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
