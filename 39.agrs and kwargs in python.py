# when we define any function we need to pass an argument for output.
# def function1(a,b,c,d,e):
#     print(a,b,c,d,e)
# function1("abc","pqr","xyz","lmn","qwe")

# If i added/print one more argument in function1 then we have to define extra letter in above func definition.
# otherwise it will show error message.
# output :TypeError: function1() takes 5 positional arguments but 6 were given

# But if i want to add lack of items it is not posibble to add normal argument,thats why we use args

# keep in mind..always in the flow of Normal args,*args,**kwargs
# we can named with any other letter also like *argskajal or **kwargskaju

def funargs(normal,*argskajal,**kwargskaju):
    print(normal)
    for item in argskajal:
        print(item)
    print("\n Now I would like to introduce some of our heroes")
    for key,values in kwargskaju.items():
        print(f"{key} is a {values}")


list1=["kajal","Preru","prashant","abhishek"] #it goes to function always in the form of tuple.
normal="I am normal argument and the students are:"
kw={"rohan":"monitor","harry":"Fitnessr Instructor"}
funargs(normal,*list1,**kw)

# output:
# I am normal argument and the students are:
# kajal
# Preru
# prashant
# abhishek
#
#  Now I would like to introduce some of our heroes
# rohan is a monitor
# harry is a Fitnessr Instructor

