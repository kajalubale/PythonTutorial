# What is the join method in Python?
# "Join is a function in Python, that returns a string by joining the elements of an iterable,
# using a string or character of our choice."

# In the case of join function, the iterable can be a list, dictionary, set, tuple, or even a string itself.
# The string that separates the iterations could be anything.
# It could just be a comma or a full-length string.
# We can even use a blank space or newline character (/n ) instead of a string.

lis = ["john","cena","khali","randy","ortan","sheamus","jinder mahal"]
# suppose i want to write like john and cena and khali and so no , then we write it as
# for item in lis:
#     print(item,"and", end="")# end it used to ignore new line

# simply we can use join method
a = " and ".join(lis)
print(a)

b = " , ".join(lis)
print(b)

#output :
# john and cena and khali and randy and ortan and sheamus and jinder mahal
# john , cena , khali , randy , ortan , sheamus , jinder mahal