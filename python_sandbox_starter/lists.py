# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# constructor
# numbers2 = list((8,9,10,11,12))


# Get a value
print(fruits[1])

# get length
print(len(fruits))

# append

fruits.append('Mangos')

print(fruits)

# remove
fruits.remove('Grapes')

print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')

#change value
fruits[0] = 'Blueberries'

# remove with pop
fruits.pop(2)

# reverse list
fruits.reverse()

#sort
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)

