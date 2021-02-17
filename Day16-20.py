#DAY 16                Exception handling

#Read a string, , and print its integer value; if cannot be converted to an integer, print Bad String.
#Note: You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get ascore.

#Sample Input 0
#3
#Sample Output 0
#3
#Sample Input 1
#za
#Sample Output 1
#Bad String

import sys
S = input().strip()
try:
    print (int(S))
except ValueError:
    print("Bad String")

