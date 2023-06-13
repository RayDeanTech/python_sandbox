# Python has functions for creating, reading, updating, and deleting files.

# open a file
myFile = open('myfile.txt', 'w')

# get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# write to file
myFile.write("I love Python")
myFile.write(" and JavaScript")
myFile.close()

# append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)