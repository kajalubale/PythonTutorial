# Instance variables
# When an object is created with the use of the new keyword, instance variables are created. They destroyed when the object is destroyed.
# Instance, variables can be accessed by calling the variable name inside the class. ObjectReference.VariableName
# Every instance of the class has its own copy of that variable. Changes made to the variable don't affect the other instances of that class.

# Class variables
# When the program starts, static variables are created and destroyed when the program stops.
# Static variables can be accessed by calling using a class name. ClassName.VariableName.
# There is only one copy of that variable that is shared with all instances of the class. 
# If changes are made to that variable, all other instances will be affected.

# Every object in Python has an attribute which is denoted by __dict__, it maps the attribute name to its value. 
# This dictionary is used to stores all the attributes defined for the object itself. Following is the syntax of using __dict__:

class Employee:
    no_of_leaves =8 # class variable are owned by the class directly,means that they are not tied to any object oo instance
    pass

harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=455
harry.role="Instructor"
harry.no_of_leaves =10 #instance variable are the variable for which the value of the variable is different for every instance.
print(harry.no_of_leaves) # this object or instance of can access the class variable globally.
print(Employee.__dict__)
print(harry.__dict__)


rohan.name="Rohan"
rohan.salary=3445
rohan.role="student"
print(harry.salary)



