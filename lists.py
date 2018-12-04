# lists is a collection which is ordered and changeable, allows duplicate members

# create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oragnes', 'Grapes', 'Pears']
# use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

print(fruits[1])

#get length
print(len(fruits))

# append to list (add)
fruits.append('Mangos')

# remove
fruits.remove('Grapes')

# insert into specific position
fruits.insert(2, 'Strawberries')

fruits.pop(3)

# reverse the list
fruits.reverse()

# sort list
fruits.sort(reverse=True)

# change value
fruits[0] = 'Blueberries'

print(fruits)