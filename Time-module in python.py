# The Execution time of program is defined as the system's time to execute the task.
# As we know all the program take some execution time,but we don't know how much,
# so this time will known with the help of time module.

# As defined " Time module handles time-related tasks. "
# It can be accessed by  simply using an [ import  time ] statement.

# In Python, time can be tracked through its built-in libraries.
# The time module consists of all time-related functions.
# It also allows us to access several types of clocks required for various purposes.
# We will be discussing some of these important functions that are commonly used and come handy for further
# programming.

# time.time():
# It returns us the seconds of time that have elapsed since the Unix epoch.
# In simple words, it tells us the time in seconds that have passed since 1 January 1970.
# Its syntax is simple and easy to use.

import time
seconds = time.time()
print("seconds since epoch :",seconds)
time.asctime()
# output : seconds since epoch : 1594985041.226975

# We use the function time.asctime() to print the local time onto the screen.
# There are a lot of other ways to do it but time.asctime() prints the time in a sequence
# using a 24 characters string.
# The format will be something like this: Mon Feb 10 08:01:02 2020

# Time.sleep():
# What sleep() function does is, it delays the execution of further commands for given specific seconds.
# In simple terms, it sends the program to sleep for some defined number of seconds.
# sleep() function is mostly used in programs directly connected to the operating system and in game development.
# It halts the program execution, giving other programs a chance to get executed simultaneously.

time.sleep(5)
# The number of seconds is sent as a parameter within parenthesis.
# The program will go to sleep for 5 seconds after getting to this line of code and will
# continue its execution afterward.

# time localtime():
# The time.localtime() is used to converts the number of seconds to local time.
# This function takes seconds as a parameter and returns the date and time in time.struct_time format.
# It is optional to pass seconds as a parameter.
# If seconds is not provided, the current time will be returned by time() is used.
import time

print ("time.localtime() returns: %s",time.localtime())

# output: time.localtime() returns: %s time.struct_time(tm_year=2020, tm_mon=7, tm_mday=17, tm_hour=17, tm_min=3, tm_sec=8, tm_wday=4, tm_yday=199, tm_isdst=0)

# We can use the time module

# In games where missions depend on a certain time limit.
# To check the execution time a certain part of our code is taking.
# To print the date or local time onto the screen
# To suspend the execution of python thread.
# To measure the efficiency of the code.

import time
initial=time.time()

k=0
while(k<45):
    print("This is kajal ubale")
    time.sleep(2)
    k+=1
print("while loop ran in",time.time() -initial,"seconds")

initial2=time.time()
for i in range(45):
    print("this is kajal")
print("For loop ran in",time.time() -initial2,"seconds")