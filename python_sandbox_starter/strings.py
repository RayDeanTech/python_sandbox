# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37


# String Formatting

print("Hello, my name is " + name + ' and I am ' + str(age) + " years old.")


# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')



# String Methods
s = 'hello world'

print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.replace('world', 'everyone'))
sub = 'h'
print(s.count(sub))
print(s.startswith('hello'))
print(s.endswith('d'))
print(s.split())
print(s.find('r'))
print(s.isalnum()) # the space makes this false
print(s.isalpha()) # the space makes this false
print(s.isnumeric())




