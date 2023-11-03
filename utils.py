# Variables
name = "Hugo"
something_is_true = True
values: list[int] = [1, 2, 3]

### Conditionals
if 1 == 1: # writes a if block
    pass
elif 1 == 2:
    pass
else:
    pass

### Loops
for value in values: # writes a for block
    pass

while something_is_true: # writes a while loop
    pass

### Functions
def my_function(parameter_one, parameter_two): # declares a function
    """This is a new function""" ## Docstring
    pass

# Dictionary
dictionary = { "Hugo": 123 }
dictionary['Hugo']
dictionary['New Entry'] = 456

# Arrays
array = [1, 2, 3, 4, 5]

# Tuples
tuple = (1, 2, 3, 4, 5)

# Array slicing
sliced = array[1:3] # [2, 3]
# Array reverse
reversed = array[::-1] # [5, 4, 3, 2, 1]


# Useful functions
len() # Gives the length of a string
type() # Gives the type of a variable
str() # Converts to string
round() # Rounds integer or float
input() # gets input from the user on terminal
print(f"") # prints to the terminal

# Classes
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Grrr")

# Sub classes
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Woof")