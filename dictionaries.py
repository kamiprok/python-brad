# dictionary is a collection which is unordered, changeable and indexed, no duplicate member

# create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# use constructor
person2 = dict(first_name='Sara', last_name='Connor')
#print(person2)

print(person, type(person))

# get value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-555-555'

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# remove item
del(person['age'])
person.pop('phone')

# clear
person.clear()

# get length
print(len(person2))

# list of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25},
]

print(people)
print(people[1]['name'])
print(person)


