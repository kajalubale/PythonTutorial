# ---MAP---

# MAP function executes certain instruction or functionality provided to it on every item of an iterable.
# suppose we created list item in string format and i want to convert it in integer then we use:

numbers=["10","3","6","4"]
# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
#     print(type(numbers[i])
# output:
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'int'>

# instead of writing this for loop we can write it in one line code
numbers=map(int,numbers)
print(numbers)
# output : <map object at 0x002D1610> map function shows output in  the form of objects
numbers=list(map(int,numbers))
print(numbers)
# output : [10, 3, 6, 4] shows in the list format.

#suppose we created one function
# def sq(a):
#     a*a
# num=[2,3,4,5,6,7,8,9,10]
# square = list(map(sq,num))
# print(square)
# output : [None, None, None, None, None, None, None, None, None]

# num=[2,3,4,5,6,7,8,9,10]
# square=list(map(lambda x:x*x,num))
# print(square)
# output : [4, 9, 16, 25, 36, 49, 64, 81, 100]

def square(a):
    a*a
def cube(a):
    a*a*a
func=[square,cube]
# num=[2,3,4,5,6,7,8,9,10]
for i in range(0,5):
    val = list(map(lambda x:x(i), func))
    print(val)
# output :
# [0,0]
# [1,1]
# [4,8]
# [9,27]
# [25,125]

# -----------FILTER---------------
# A filter function in python tests a specific user-defined condition for a function and
# returns an iterable for the element and values that satisfy the condition or, in other words, return true.

a=[1,2,3,4,5,6]
b=[2,5,0,3,4,55,5]
c=list(filter(lambda x:x in a,b))
print(c)
# first list compare with second list and shows equal value and vise verrsa
# output : [2, 5, 3, 4, 5]

list_1=[1,2,3,4,5,6,7,8]
def is_greater_5(num):
    return num>5

gr_than_5 =list(filter(is_greater_5,list_1))
print(gr_than_5)
# output : [6, 7, 8]

#-------------------REDUCE----------
# Reduce Functions apply a function to every item of an iterable and gives back a single value as a resultant.
# we have to import Reduce function from functools module
from functools import reduce
list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x*y,list1)
print(num)
# output : 48