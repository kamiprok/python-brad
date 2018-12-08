# python has functions for creating, reading, updating and deleting files

# open file
myFile = open('myfile.txt', 'w')

# get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()
print('Is Closed: ', myFile.closed)

# append to file (open again would override it)
myFile = open('myfile.txt', 'a')
myFile.write(' cos tam cos tam')

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)


