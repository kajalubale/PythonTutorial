# module can be defined as a file containing a runnable python code.
# module can be function, classes or variables.

# Two Types of module : Built in and external
# Built-in modules are already installed in python by default.
# Examples:
# 1.calendar : used in case we are working with calendars
# 2.random : used for generating random numbers within certain defined limits.
# 3.enum : used while working with enumeration class
# 4.html : for handling and manipulating code in html
# 5.math : for working with match function such as sin,cos,etc
# 6.runpy : runpy is an important module as it locates and runs python modules without importing then first.

# External modules have to be downloaded externally and can be done by using command "pip install module_name"

import random
random_number=random.randint(0,5)
print(random_number) # shows random number from 0 to 5

lst = ["star plus","DDI","AAJtak"]
choice=random.choice(lst)
print(choice)