# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object


# create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My Name Is {self.name} and I am {self.age}"

    def has_birthday(self):
        self.age += 1


# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My Name Is {self.name} and I am {self.age} and my balance is {self.balance}'


# init user object
ray = User("Ray Dean", "ray@email.com", 69)

# init customer object
janet = Customer("Janet Johnson", "janet@dammit.com", 42)

janet.set_balance(500)
print(janet.greeting())


ray.has_birthday()

print(ray.greeting())
