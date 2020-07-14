# F string is new string formatting approach called formatted string literals or "f-string
# They are indicated by an "f" before the quotation mark of a string.
# put the expession inside{} to evaluate the result.

str1="python"
str2="programming"
print(f"Here is {str1} and {str2} tutorial")

# output: Here is python and programming tutorial

import math
me="abc"
c="111"
a=f"This is  {me} having score{c} {math.cos(65)}"
print(a)

# output : This is  abc having score111 -0.562453851238172