name = 'Brad'
age = 37

# concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# string formatting

# arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-strings
print(f'Hello, my name is {name} and I am {age}')

# string methods

s = 'hello world'

# ca[ota;oze string
print(s.capitalize())
print(s.upper())