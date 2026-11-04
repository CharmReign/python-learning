"""
Lesson 2: Basic Data Types
===========================
Run this file:  python 01_fundamentals/02_data_types.py
"""

# int: whole numbers (no size limit in Python, unlike Java's int/long)
items_in_cart = 3
huge = 10 ** 30
print(items_in_cart, huge)

# float: numbers with a decimal point
price = 19.99
print(price)

# str: text, in "double" or 'single' quotes (both are the same in Python)
city = "Manila"
greeting = 'Hello'
print(greeting, city)

# bool: True or False (capital T/F, unlike Java's true/false)
is_logged_in = True
has_paid = False
print(is_logged_in, has_paid)

# None: "no value yet" (like Java's null)
middle_name = None
print(middle_name)

# type() tells you what type a value is
print(type(items_in_cart))   # <class 'int'>
print(type(price))           # <class 'float'>
print(type(city))            # <class 'str'>
print(type(is_logged_in))    # <class 'bool'>
print(type(middle_name))     # <class 'NoneType'>

# --- Converting between types ---------------------------------------------
age_text = "30"              # this is TEXT, not a number
age_number = int(age_text)   # convert text -> int
print(age_number + 1)        # 31

print(str(42) + " apples")   # convert int -> text to join with text
print(float("3.5"))          # text -> float
print(int(9.99))             # float -> int CUTS OFF the decimals: 9 (no rounding)

# Common beginner bug: mixing text and numbers
# print("Age: " + 30)        # TypeError! can't add str and int
print("Age: " + str(30))     # fix 1: convert
print(f"Age: {30}")          # fix 2: f-string (preferred, more in Lesson 3)
