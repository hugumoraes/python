# -------------- Imports -------------- #
import pandas
import random

# -------------- Imports -------------- #

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
    
# -------------- Files -------------- #
# Read = r
# Write = w
# Append = a
# Read and Write = r+

# Open
file = open("<file>.<ext>")
# Read
contents = file.read()
# Close
file.close()
# Write
file.write("<text>")

# Using with
with open("<file>.<ext>") as file:
    contents = file.read()

with open("<file>.<ext>", mode="a") as file:
    file.write("<text>")

# -------------- Files -------------- #

# -------------- Pandas (CSV) -------------- #
data = pandas.read_csv('<path>.csv')

# Get Data in Columns
data['temp']

# Get Data in Rows
data[data.day == 'Monday']

# Create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv('<path>.csv')

### How to iterate over a Pandas dataframe
student_dict = {
    'student': ['Amy', 'James', 'Angela'],
    'score': [76, 56, 65]

}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.student == 'Angela':
        print(row.score)

# -------------- Pandas (CSV) -------------- #

# -------------- List Comprehension -------------- #
### List Comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers] # [2, 3, 4]

### Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5] # ["Alex", "Beth", "Dave"]

### Dictionary Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names} 
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60} 

# -------------- List Comprehension -------------- #