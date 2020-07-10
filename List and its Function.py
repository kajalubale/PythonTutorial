#################################### List and its Functions ###########################################

# Most versatile Data Type of Python is the list,
# which can be written as a list of comma-separated values (items) between square brackets.
# Lists might contain items of different types, but usually the items all have the same type.

# Ex:
grocery=["vimbar","harpic","deodrant",'lollypop',56,4.56]
print(grocery)
#output : ['vimbar', 'harpic', 'deodrant', 'lollypop', 56, 4.56]

# The above list contains strings, integer and even float type data.
# It means above list contains any kind of data means it’s not mandatory to form list of only one data type.
# List can contain any kind of data in it.

# List elements are also accessed by using Indexes
# i.e. first element of list possess 0 index then second as 1 and so on.

# Note : if you put any index which isn’t in the list
# i.e. that index is not there in list then you will get an error.

print(grocery[5])
#output :4.56

#print(grocery[7])
#output : IndexError: list index out of range

# List Methods :

numbers=[2,4,5,6,7,8,8]
numbers.remove(8) #remove 8 from list
print(numbers)
#output : [2, 4, 5, 6, 7, 8]

#numbers=[2,4,5,6,7,8,8]
#numbers.remove(8,8)
#print(numbers)
#output : TypeError: remove() takes exactly one argument (2 given)

numbers=[2,3,4,5,6,7]
numbers.pop() #removes last element
print(numbers)
#output: [2, 3, 4, 5, 6]

num=[2,7,11,9,3]
print(num.pop(2))#this will delete and return index 11 value
#output : 11
print(num)#shows list without 11 value
#output : [2, 7, 9, 3]

num=[3,4,2,1,6,8,9,11]
num.sort() #will sort the list
print(num)
#output : [1, 2, 3, 4, 6, 8, 9, 11]

num=[3,4,2,1,6,8,9,11]
num.reverse() #will reverse the list
print(num)
#output : [11, 9, 8, 6, 1, 2, 4, 3]

num=[3,4,2,1,6,8,9,11]
num.append(12) #will add 12 in the last of list
print(num)
#output : [3, 4, 2, 1, 6, 8, 9, 11, 12]

numbers = [] # Blank List
numbers.append(1) # will add 1 in the last of list
numbers.append(5) # will add 5 in the last of list
print(numbers)
# Output : [1, 5]

numbers = [] # Blank List
numbers.append(1) # will add 1 in the last of list
numbers.append(5) # will add 5 in the last of list
print(numbers)
# Output : [1, 5]

num=[2,3,4,5,6,6,7,8]
num.insert(2,89) #will add 89 at index 2 in list
print(num)
# Output : [2, 3, 89, 4, 5, 6, 6, 7, 8]

# List Slicing :

# List slices, like string slices are the sub part of a list extracted out.
# You can use indexes of list elements to create list slices as per following format :

# Seq=list[start:stop:step]

numbers = [2, 7, 9, 11, 3]
print(numbers[0:5]) # Output : [2, 7, 9, 11, 3]
print(numbers[:5]) # Output : [2, 7, 9, 11, 3]
print(numbers[:]) # Output : [2, 7, 9, 11, 3]
print(numbers[1:]) # Output : [7, 9, 11, 3]
print(numbers[1:4]) # Output : [7, 9, 11]
print(numbers) # Output : [2, 7, 9, 11, 3]

# Extended Slice
# Default: 1st Parameter is 0, 2nd Parameter is Length of list, 3rd Parameter is 1

print(numbers[::]) # Output : [2, 7, 9, 11, 3]
print(numbers[::1]) # Output : [2, 7, 9, 11, 3]
print(numbers[::3]) # Output : [2, 11]

# Negative Step works only if first two parameters are blank
print(numbers[::-2]) # Output : [3, 9, 2]
print(numbers[0:3:-2]) # Output : [] / blank list
# So don't take any negative value as third parameter except -1

print(len(numbers)) # print length of list
# Output : 5
print(max(numbers)) # Output : 11
print(min(numbers)) # Output : 2

print(numbers) # Output : [2, 7, 9, 11, 3]
numbers[1] = 98
print(numbers) # Output : [2, 98, 9, 11, 3]

######### Tuple ##############

# Mutable - can change
# Immutable - cannot change

tp = (1, 2, 3)
print(tp) # Output: (1, 2, 3)
# tp[1] = 8 #=> Error : because tuple values can't be changed

# Tuple with single Value
# tp = (1) # it act as variable so for tuple ',' required
tp = (1,)
print(tp) # Output : (1,)

# Swap in Python
a = 1
b = 8
# Generally we do this
# temp = a
# a = b
# b = temp

# In Python very simple
print(a, b) # Output : 1 8
a,b = b,a
print(a, b) # Output : 8 1