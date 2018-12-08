# loops are used for iterating over a sequence( list, tuple, dictionary, set, string)

people = ['John', 'Paul', 'Sarah', 'Susan']

# simple for loop

for person in people:
    print(f'Current person: {person}')

# break

for person in people:
    if person == 'Sarah':
        break
    print(f'Current person: {person}')

# continue

for person in people:
    if person == 'Sarah':
        continue
    print(f'Current person: {person}')

# range

for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

# while loop executes a set of statements as long as a condition is true

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1


