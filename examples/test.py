import sys
import os

# Add the parent directory (project) to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



# magic method new and init 
from python_oop import main

obj = main.NewMethodExample()


meta = main.Example()


Person = main.Person("Alice", 30)


# Usage
book1 = main.Book("1984", "George Orwell")
book2 = main.Book("1984", "George Orwell")
print(book1 == book2)  # Output: True