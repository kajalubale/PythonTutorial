############### Exercise 4 : Astrologer's Stars ########

# Question :

## Pattern Printing ##

# Input :

# Integer n
# Boolean = True or False

# Expected Output :

# Given: True n=4
# Output:
# *
# **
# ***
# ****

# Given: False n=4
# Output:
# ****
# ***
# **
# *

# Solve Here :
# print("pattern printing")
# while(True):
#     num=int(input("Enter number how many rows you want : "))
#     print("enter 1 or 0 :")
#     bool_val= input("1 for True or 0 for False :")
#
#     if bool_val=="1":
#             pattern =  True
#             if pattern:
#                 for i in range(0,num+1):  # start  from 0 and end at num+1
#                     print("*"*int(i))
#     if bool_val=="0":
#             pattern = False
#             if not pattern:
#                 for i in range(num,0,-1):  # start  from num and end at 0 ,for reverse -1
#                     print("*"*int(i))
#     continue

a=int(input("please add number of line you want to print"))
b=bool(int(input("please add 0 for false")))

def star(a,b):
    if b==True:
        c=1
        while c<=a:
            print(c * "*")
            c=c+1
    else:
        while a>0:
            print(a* "*")
            a=a-1
star(a,b)