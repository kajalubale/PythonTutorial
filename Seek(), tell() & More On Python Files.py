########### Seek(), tell() & More On Python Files ############

## Set Up Steps for this tutorial :=>
# Make a File "seek.txt"
# Add few lines of text in it.

f = open("seek.txt")# created new text file
# f.tell() tells us where is file pointer currently in file
# first charcter is at 0 index in file

print(f.tell())
# output: 0

print(f.readline())
# output: Can we build atmanirbhar district in india?

# f.seek() is used to reset file pointer
f.seek(7) # move file pointer to 7th index
print(f.readline())
# Print First Line in the File from index 7
# Output : build Aatmnirbhar Districts in India ?

print(f.tell())  # Now file pointer on second line starting
# Output : 47
print(f.readline())
# Print Second Line in the File
# Output : Can we make Competitive Problem Soving Paltform for Core Engineering Students ?

print(f.tell())  # Now file pointer on third line starting
# Output : 128

print(f.readline())
# Print third Line in the File
# Output : What are your views ?

f.close()
