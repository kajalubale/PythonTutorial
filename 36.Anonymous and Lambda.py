# if a program has a large piece of code that is required to be executed repeatedly,
# then we use function to improve code reusability,modularity and integrity.

def minus(x,y):
   print(x-y)
minus(7,2)

#instead of using this function we can use lambda
minus=lambda x,y:x-y
print(minus(9,4))

# Anonymous function or lambda expression is a function definition
# that is not bound to an identifier(def).
# The anonymous function is an inline function.
# It is created using lambda operator and cannot contain multiple expression.

result=lambda n1,n2,n3:n1+n2+n3
print("sum of three values : ",result(10,15,16))

# python List Sort():
# Sorting means arranging data systematically.
# syntax : list.sort(key=myFunc , reverse=True|False)
# key : In the key parameter, we specify a function that is called on each list element before making comparisons.
# reverse : This is optional.False will sort the list in ascending order,and True will sort in Descending order.
# Default is reverse=False.

a=[[1,14],[5,6],[8,3]]
a.sort(key=lambda x:x[1])
print(a)
