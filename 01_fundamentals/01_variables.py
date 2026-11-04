"""
Lesson 1: Variables
====================
Run this file:  python 01_fundamentals/01_variables.py
Read the comments, run it, then CHANGE things and run it again.
"""

# A VARIABLE is a name that points to a value.
# The "=" sign means "assign" (store), NOT "equals" like in math.
name = "Reign"
age = 25

print(name)
print(age)

# You can reuse a variable: it now points to a new value.
age = 26
print("Next year:", age)

# Python figures out the type for you (this is "dynamic typing").
# In Java you'd write:  String name = "Reign";  int age = 25;
# In Python there's no type keyword and no semicolon.

# A variable can even point to a different TYPE later (allowed, but usually a bad idea):
score = 10
score = "ten"
print(score)

# --- Naming rules ---------------------------------------------------------
# Allowed:   letters, digits, underscores; can't START with a digit
# Python convention is snake_case (Java uses camelCase):
first_name = "Ada"          # good, Pythonic
total_price = 99.5          # good
# firstName = "Ada"         # works, but not the Python style
# 2nd_place = "Bob"         # ERROR: can't start with a digit
# class = "A"               # ERROR: "class" is a reserved keyword

# Constants: Python has no "final" keyword. By convention, ALL_CAPS
# tells other developers "don't change this".
MAX_LOGIN_ATTEMPTS = 3

# Multiple assignment in one line
x, y, z = 1, 2, 3
print(x, y, z)

# Swap two values without a temp variable (in Java you'd need one)
x, y = y, x
print("After swap:", x, y)
