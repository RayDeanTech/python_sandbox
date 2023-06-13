# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dictionary
person = {"first_name": "John", "last_name": "Doe", "age": 30}

# use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# print(person2, type(person2))

# get value
print(person["first_name"])
print(person.get("last_name"))

# add key/value
person["phone"] = "555-555-5555"

# get dictionary keys
print(person.keys())

# get dictionary items
print(person.items())


# copy dictionary
person2 = person.copy()
person2["city"] = "Boston"


# remove item
del person["age"]
person.pop("phone")

# clear
person.clear()

# get length
print(len(person2))

# list of dicts
people = [
    {"name": "Martha", "age": 30},
    {"name": "Kevin", "age": 25}
]


print(people[1]['name'])
