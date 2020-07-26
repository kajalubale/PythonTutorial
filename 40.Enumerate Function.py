# An enumerate is a built-in function that provides an index to data structure elements,
# making iterations through them easier and simpler.

# Syntax:
# enumerate(iterable, start=0)

# When calling a simple enumeration function, we have to provide two parameters:

# The data structure that we want to iterate
# The index from where we want to start our iteration

# Example of enumerate using a python list.
# We can iterate over the index and value of an item in a list by using a basic for loop with enumerate().

list1=["bhindi","aloo","paneer","methi","palak"]
# if i want to buy only odd number values like bhindi,paneer,palak
i=1
for item in list1:
    if i%2!=0:
        print(f"jarvis please buy {item}")
    i+=1

# instead for writing this whole code it can simply write it by using enumerate function.
for index,item in enumerate(list1):
    if index%2==0:
        print(f"jarvies please buy {item}")

# Example:
list_1=["code","with","harry"]
for index,val in enumerate(list_1):
    print(index,val)

#Example:
list_2 = ["Python", "Programming", "Is", "Fun"]
#Counter value starts from 5
result = enumerate(list_2,5)
print(list(result))

# Advantages of using Enumerate:
# It is a built-in function
# It makes the code shorter
# We do not have to keep count of the number of iterations
# It makes the implementation of for loop simpler and cleaner
# Lesser code so lessor chances of error and bugs
# We can loop through string, tuple or objects using enumerate
# We can start the iteration from anywhere within the data structure as we have the option of providing the starting index for iteration.