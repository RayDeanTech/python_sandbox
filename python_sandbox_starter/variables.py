# A variable is a container for a value, which can be of various types

'''
This is a
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# NO SEMI COLONS!!!!!!!!!!!!!!!!!!!!!!!!

# x = 1           # int, casted as int by default
# y = 2.5         # float
# name = 'John'   # string
# is_cool = True  # bool, REQUIRES initial caps

# multiple assignment

x, y, name, is_cool = (1, 2.5, 'John', True)


# Basic Math

a = x + y

print('===')
print(type(x), x)
print(type(y), y)

# casting
x = str(x)
y = int(y)
z = float(y)

print('===')
print(type(x), x)
print(type(y), y)
print(type(z), z)
