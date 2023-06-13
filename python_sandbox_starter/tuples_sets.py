# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', "Oranges", 'Grapes' ))

# single value needs trailing comma
fruits2 = ('Apples',) # IMPORTANT:  a trailing comma is required for this to be TUPLE, dog.
# print(fruits2, type(fruits2))

# get value
print(fruits[1])

# Can't change TUPLE values
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# check if in set
print('Apples' in fruits_set)

# add to set
fruits_set.add('Grape')

# remove from set
fruits_set.remove('Grape')

# add duplicate
fruits_set.add('Apples')  # no error dump.  I just won't add it twice.

# clear set
# fruits_set.clear()

# delete
# del fruits_set

print(fruits_set)