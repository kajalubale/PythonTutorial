# Create a dictionary of 5 Words
# Take input from the user
# Return the meaning of the word from the dictionary

dict={"a":"apple","b":"ball","c":"cat","d":"doll","e":"elephant"}
user_input = input("Enter the word from above dictionary : ")

if user_input == 'a':
    print(dict["a"])
elif user_input == 'b':
    print(dict["b"])
elif user_input == 'c':
    print(dict["c"])
elif user_input == 'd':
    print(dict["d"])
elif user_input == 'e':
    print(dict["e"])
else:
    print("no such word exists in dictionary")

print(user_input,"means",dict[user_input])

#output :
#Enter the word from above dictionary : a
#apple
#a means apple