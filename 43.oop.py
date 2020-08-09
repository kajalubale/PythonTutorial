# A class is a collection of objects, and an object is defined as an instance of class possessing attributes. 
# The object is an entity that has state and behavior.
#  A class has all the similar attributes, like if we have a class students, 
# then it will only consist of students related data, such as subjects, names, attendance ratio, etc.

# Along with classes and objects, you will learn many new terminologies related to OOP in further tutorials.
#  Some of these terminologies are:

# Instances
# Constructor
# Methods
# Abstraction
# Inheritance

# By using oop, we can divide our code into many sections known as classes.
#  Each class holds a distinct purpose or usage. 
# For example, if we have created a class named "Books" then all the attributes it possesses should 
# be related to books such as the number of pages, publishing date or price, etc.


#  Object-oriented programming /vs
#  1. Object-oriented programming is the problem-solving approach. The computation is done by using objects.
#  2. OOP makes development and maintenance easier.
#  3. OOP provides a proper way for data hiding. It is more secure than procedural programming. You cannot access private data from anywhere.
#  4. Program is divided into objects

# Procedure Oriented Programming
# 1. It is Structure oriented. Procedural programming uses a list of instructions. It performs the computation step by step.
# 2. When the project becomes lengthy, it is not easy to maintain the code.
# 3. Procedural programming does not provide any proper way for data binding, so it is less secure. In Procedural programming, we can access the private data.
# 4. The program is divided into functions.

# creating our first python program

class student:
    pass #pass means nothing but it will not shows error
harry=student() #harry and larry are the objects.
larry=student()
harry.name="harry"
harry.std="10th"
harry.marks="500"
print(harry.std,harry.marks)
# output : 10th 500
