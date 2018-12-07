# if/else conditions are used to decide to do something based on something being true or false
# comparision operators ==, !=, >, <, >=, <=
# logical operators and, or, not
# membership operators not, not in


x = 13
y = 20

# simple if, else, elif


if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# nested if

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and lest or equal to 10')

# logical operators: and, or

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and lest or equal to 10')

if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and lest or equal to 10')

# not

if not(x == y):
    print(x, '!=', y)

# membership operators: not, not in (lists etc)

numbers = [1, 2, 3, 4, 5]

if x in numbers:
    print(x in numbers)

if x not in numbers:
    print(x not in numbers)

# identity ops: is, is not

if x is not y:
    print(x is not y)



