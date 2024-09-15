# magic method 



class NewMethodExample:
    """
    This class demonstrates the use of the __new__ magic method, which is used 
    to create an object of the class before __init__ initializes it.
    __new__ is useful for handling immutable data or for implementing 
    singleton patterns, or when metaclasses are involved.
    """
    def __new__(cls):
        print("Creating new instance ...")
        return super(NewMethodExample, cls).__new__(cls)
    
    def __init__(self):
        print("Initializing instance ...")



# Another example for new method example 

class MyTuple(tuple):
    def __new__(cls, iterable):
        return super(MyTuple, cls).__new__(cls, iterable)

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class Example(metaclass=Meta):
    pass



# Object Representation 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}, aged {self.age}"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
    


# Comparison Magic Methods
# __eq__(self, other): Equality (==).
# __ne__(self, other): Inequality (!=).
# __lt__(self, other): Less than (<).
# __le__(self, other): Less than or equal to (<=).
# __gt__(self, other): Greater than (>).
# __ge__(self, other): Greater than or equal to (>=).



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author



