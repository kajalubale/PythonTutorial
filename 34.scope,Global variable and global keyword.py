# scope: scope  referes to the coding area where particular python variable is accessible.
x=30 # global variable scope
def function1():
    x=10 # local variable/scope
    m=20 # local variable/scope
    print(x)
    print(m)
function1()
print(x)

# output :
# 10
# 20
# 30

# A variable which is declared inside a function or loop is called local variable
# A variable which is accessed anywhere in program is called global variable

x=30 # global variable scope
def function1():
    # x=10 # local variable/scope # if is not present in function then it take global variable value and show output 30
    m=20 # local variable/scope
    print(x)
    print(m)
function1()
print(x)

# Firstly local variable check in program if not presents,shows global variable value.
# if we want to modify global variable inside the function then we use global keyword.
# Global Keyword : It is used to create a global variable and make changes to the variable in a local scope.
# Rules:
# If we assigned a value to a variable within function body,it would be local unless explicitly declared as global.
# Those variables that are reference only inside a function are implicitly global.
# There is no need to use the global keyword outside a function.

x=23
def kajal():
    # global x
    x=26
    print(x)
kajal()
print(x)
# output: 26
# if i comment on global x it changes value to 23, that means we can change global value inside the function.

# when we define function inside another function,it become a nested function.
# we already know how to access a global variable from a function by using a Global keyword.
# when we declare a local variable in a function,its scope is usually restricted to that function alone.
# This is because each function and subfunction stores its variables in its separate workspace.

x=89
def kajal1():
    x=20
    def kajal2():
        global x
        x=88
        print("Before calling kaja2()",x)
    kajal2()
    print("After calling kaja2()",x)
kajal1()
print(x)