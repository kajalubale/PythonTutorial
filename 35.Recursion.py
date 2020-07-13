# Recursion: Using Function inside the function, is known as recursion

def print_2(str):
    print("This is",str)
print_2("kajal")
# output: This is kajal

# but if i used print_2("str") inside the function it shows Recursion error.
# def print_2(str):
#     print_2(str)
#     print("This is",str)
# print_2("kajal")
# output :   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# Factorial program using Recursive and iterative
# n!= n*n-1*n-2*n-3......1
# n!=n*(n-1)!
def factorial_iterative(n):
    '''

    :param n: integer
    :return: n * n-1 * n-2.....1
    '''
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return  fac
def factorial_Recursion(n):
    '''

    :param n: Integer
    :return: n * n-1 *n-2.....1
    '''
    if n==1:
        return 1;
    else:
        return n * factorial_Recursion(n-1)
    # 5 * factorial_Recursion(4)
    # 5 * 4 * factorial_Recursion(3)
    # 5 * 4 * 3 * factorial_Recursion(2)
    # 5 * 4 * 3 * 2 * factorial_Recursion(1)

# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number=int(input("Enter the number:"))
print("Factorial using iterative : ",factorial_iterative(number))
print("Factorial using Recursion : ",factorial_Recursion(number))
print("Fibonacci of number : ",fibonacci(number))