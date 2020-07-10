# if condition=true goto elif condition=true
# if condition=flase goto else

var1=10;
var2=20;
var3=int(input("Enter var3 value :"))
if var3>=(var1 and var2): # if both conditions satisfied
    print("Var3 is greater")
elif var3==(var1 and var2):
    print("equal")
else:
    print("Var3 is lesser")

list1=[1,2,3,4,9,6]
if 15 not in list1:
    print("No its not in list")
    
# Quiz
# Ques : Write program to check whether 
# you are above,equal to or less than 18.
# Give a sample allowed task to each age group

age = int(input("Enter your age: "))
if age<18:
    print("You cannot drive")
elif age==18:
    print("we will think about you")
else:
    print("you can drive")

