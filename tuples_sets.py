# tupple is a collection which is odered and unchangeable. allows duplicate members

# create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# single value needs trailing comma
fruits2 = ('Apples')
fruits3 = ('Apples',)

print(fruits2, type(fruits2))
print(fruits3, type(fruits3))

# get value
print(fruits[1])

# CAN'T change value
# fruits[0] = 'Rears'

del fruits2
# print(fruits2)

print(len(fruits))

#### set is collection which is unordered and unindexed, no uplicate members

# create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# check if in set
print('Apples' in fruits_set)

# add to set
fruits_set.add("Grapes")

# remove from set
fruits_set.remove('Grapes')

# add duplicate
fruits_set.add('Apples')

# clear set
#fruits_set.clear()

# delete set
#del fruits_set

print(fruits_set)