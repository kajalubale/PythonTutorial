# Create one text file name as (kajal.txt)
# To open kajal.txt (external file)
open("kajal.txt")
# nothing shows but program runs.

# file pointer(here f) returned by open function is used to read/write in file
# "rt" is default mode so it is optional to write
# Below is same as f = open("24. Tutorial.txt")

f=open("kajal.txt")
content=f.read()
print(content)
f.close()
# Good practice to close opened files
# Technically it is to frees/release all the resources
# using by file when it is open.
# output :
# my name is kajal ubale.

# kajal ubale is sincere and .

# I am learning python from scrath.


## Reading in binary mode
f = open("kajal.txt", "rb")
content = f.read()
print(content)
f.close()

# Output : (read as binary)
# b'my name is kajal ubale.\r\n\r\nkajal ubale is sincere and .\r\n\r\nI am learning python from scrath.'

## Reading fixed length of characters
f = open("kajal.txt", "rt")
content = f.read(4)
print(content)
# Output : my n


# Now file pointer ( f ) points to 5th character and starts reading from there.
# (matlab jaha pe pointer rukha hai vaha se chalu hoga)
content = f.read(4)
print(content)
# Output : ame

f.close()

# Reading more than available characters
f = open("kajal.txt", "rt")
content = f.read(344555)
# It will print till available character
print("1 :",content)
# Output :
# 1 : my name is kajal ubale.
# kajal ubale is sincere and .
# I am learning python from scrath.

content = f.read(344555)
# Nothing left to read now
print("2 :",content)
# Output :
# 2 :
f.close()

## Printing character by character in each line

f = open("kajal.txt", "rt")
content = f.read()
for line in content:
    print(line)
f.close()
# Output :
# m
# y

# n
# a
# m
# e

# i
# s
# ...............
## Printing line by line using itreater in file

f = open("kajal.txt", "rt")
content = f.read()
for line in f:
    print(line)
f.close()
# Output : Nothing because content has already read the file

f = open("kajal.txt", "rt")
# content = f.read()
for line in f:
    print(line)
f.close()
# (print by default give a backslash end character and file also have new line charcter when we write next line in file)
# my name is kajal ubale.
# kajal ubale is sincere and .
# I am learning python from scrath.

f = open("kajal.txt", "rt")
# content = f.read()
for line in f:
    print(line,end="")
f.close()
# Output : (print by default give a backslash end character)
# my name is kajal ubale.
# kajal ubale is sincere and .
# I am learning python from scrath.


##### readline function to read one line a time

f = open("kajal.txt", "rt")
print(f.readline())
f.close()
# Output :
# my name is kajal ubale.


f = open("kajal.txt", "rt")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
# Output : (new line in file already + one line gap due to print's by default backslash)
# my name is kajal ubale.
# kajal ubale is sincere and .
# I am learning python from scrath.

########## Readlines Function to get list of lines.

f = open("kajal.txt", "rt")
print(f.readlines())
f.close()
# Output :
# ['my name is kajal ubale.\n', '\n', 'kajal ubale is sincere and .\n', '\n',
# 'I am learning python from scrath.']

######################################################