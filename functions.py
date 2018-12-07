# function is a block of code which only runs when it is called,
# we do not use curly brackets, we use indentation with tabs or spaces

# create function


def say_hello(name='Samuel'):
    print(f'Hello {name}')


say_hello("John Doe")
say_hello()

# return values


def get_sum(num1, num2):
    total = num1 + num2
    return total


print(get_sum(3,4))

num = get_sum(2,3)
print(num)

# lambda junction is a small anonymous function
# can take any number of arguments, but can only have one expression
# similar to js arrow function(!)

getsum = lambda num1, num2 : num1 + num2

print(getsum(10, 3))
