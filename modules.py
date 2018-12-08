# modules are files containing a set of functions to include in your application
# there are core python modules, modules you can install using the pip package manager(including Django)
# as well as custom modules

import datetime
from datetime import date
import time
from time import time
# pip module
from camelcase import CamelCase
# custom module
import validator
from validator import validate_email

today = datetime.date.today()

tomorrow = date.today()

print(today)
print(tomorrow)

# timestamp = time.time()

# print(timestamp)

timestamp2 = time()

print(timestamp2)

# pip module import and camelcase

c = CamelCase()

print(c.hump('hello there world'))

email = 'test@test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Email is wrong')
