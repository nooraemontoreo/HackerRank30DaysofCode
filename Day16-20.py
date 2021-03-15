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
    
    
#Write a Calculator class with a single method: int power(int,int). The power method takes two integers, and , 
#as parameters and returns the integer result of . If either or
#is negative, then the method must throw an exception with the message: n and p should be non-negative.
#Note: Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.
#Input Format
#Input from stdin is handled for you by the locked stub code in your editor. The first line contains an integer,
#the number of test cases. Each of the subsequent lines describes a test case in space-separated integers that denote andrespectively.

#Constraints: No Test Case will result in overflow for correctly written code.
#Output Format: Output to stdout is handled for you by the locked stub code in your editor. There are lines of output, where each line contains the result of
#as calculated by your Calculator class' power method.
#Sample Input

4
3 5
2 4
-1 -2
-1 3

#Sample Output

243
16
#n and p should be non-negative
#n and p should be non-negative


    
class Calculator:
    def power(self,n,p):

        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p
    
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   

