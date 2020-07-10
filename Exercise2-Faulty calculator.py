# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user and then return the result

Calculator_on = True
print('Welcome, you calculator is ready to serve you !')
while(Calculator_on == True):
    x=int(input("enter First number:"))
    y=int(input("enter second number:"))
    operator = input('Please select operator from this {*,+,/,-}:')

    #output part
    if(operator=='*'):
        if(x==45 and y==3):
            print("555")
        else:
            print(x*y)
    elif(operator=='/'):
        if(x==56 and y==6):
            print("4")
        else:
            print(x/y)
    elif(operator=='+'):
        if(x==56 and y==9):
            print("77")
        else:
            print(x+y)
    elif(operator=='-'):
        print(x-y)

    print('Do you want to calculate again?','\n','please type 1 for YES  or 0 for NO:')
    Calculator_on=int(input())
    if(Calculator_on==False):
        print('Thank you,Hope you will use me again!!! ')
