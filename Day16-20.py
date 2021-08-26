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
        
        
        
 #DAY 18                Queues and Stacks

#A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you determine if a given string, , is a palindrome?
#To solve this challenge, we must first take each character in , enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means  isn't a palindrome).
#Write the following declarations and implementations:
#Two instance variables: one for your , and one for your .
#A void pushCharacter(char ch) method that pushes a character onto a stack.
#A void enqueueCharacter(char ch) method that enqueues a character in the  instance variable.
#A char popCharacter() method that pops and returns the character at the top of the  instance variable.
#A char dequeueCharacter() method that dequeues and returns the first character in the  instance variable.
#Input Format
#You do not need to read anything from stdin. The locked stub code in your editor reads a single line containing string . It then calls the methods specified above to pass each character to your instance variables.
#Constraints
#is composed of lowercase English letters.
#Output Format
##You are not responsible for printing any output to stdout.
#If your code is correctly written and  is a palindrome, the locked stub code will print ; otherwise, it will print 

#Sample Input
              #racecar
#Sample Output
             #The word, racecar, is a palindrome.
    
import sys

class Solution:
    # Write your code here
    def __init__(self):
          self.mystack = list()
          self.myqueue = list()
          return(None)

    def pushCharacter(self, char):
        self.mystack.append(char)

    def popCharacter(self):
        return(self.mystack.pop(-1))

    def enqueueCharacter(self, char):
        self.myqueue.append(char)

    def dequeueCharacter(self):
        return(self.myqueue.pop(0))
    

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
    
    
    
    
#Day 19:                            Interfaces

#Task
#The AdvancedArithmetic interface and the method declaration for 
#the abstract divisorSum(n) method are provided for you in the editor below.

#Complete the implementation of Calculator class, 
#which implements the AdvancedArithmetic interface. 
#The implementation for the divisorSum(n) method must return the sum of all divisors of n.

#Example
#n = 25
#The divisors of 25 are 1, 5, 25. Their sum is 31.
#n = 20
#The divisors of 20 are 1 , 2, 4, 5, 10, 20 and their sum is 42.
#Input Format
# single line with an integer, n.


 
#Constraints
#1 <= n <= 1000
#Output Format
#You are not responsible for printing anything to stdout. 
#The locked template code in the editor below will call your code and print the necessary output.

#Sample Input

#6
#Sample Output

#I implemented: AdvancedArithmetic
#12
#Explanation

#The integer 6 is evenly divisible by 1, 2, 3, and 6. Our divisorSum method should return
#the sum of these numbers, which is 1 + 2 + 3 + 6 = 12. The Solution class then prints 
# I implemented: AdvancedArithmetic on the first line, 
#followed by the sum returned by divisorSum (which is 12) on the second line.


#             Python doesn't support interfaces(and doesn't need to). 
#Python has powerful multiple inheritance anyways, so languages like 
#Java which have single inheritance only have to cope by inculcating "implementable" interfaces


# hence I am using C++ here

include <cmath>
include <cstdio>
include <vector>
include <iostream>
include <algorithm>
include <string>
using namespace std;
class AdvancedArithmetic{
    public:
        virtual int divisorSum(int n)=0;
};
class Calculator : public AdvancedArithmetic {
public:
    int divisorSum(int n) {
        int s=0,i=1;
        while(i<=n){
            if(n%i==0){
            s=s+i;
            // n=n/i;
            i++;
            }
            else {
            i++;
            }
        }
        return s;
    }
};
int main(){
    int n;
    cin >> n;
    AdvancedArithmetic *myCalculator = new Calculator(); 
    int sum = myCalculator->divisorSum(n);
    cout << "I implemented: AdvancedArithmetic\n" << sum;
    return 0;
}


#Day 20:                        Sorting


#Task
#Given an array, a, of size n distinct elements, 
#sort the array in ascending order using the Bubble Sort algorithm above. 
#Once sorted, print the following 3 lines:

#Array is sorted in numSwaps swaps.
#where numSwaps is the number of swaps that took place.
#First Element: firstElement
#where firstElement is the first element in the sorted array.
#Last Element: lastElement
#where lastElement is the last element in the sorted array.
#Hint: To complete this challenge, you will need to add a variable 
#that keeps a running tally of all swaps that occur during execution.

#Example
#a = [4, 3, 1, 2]


 
#original a: 4 3 1 2
#round 1  a: 3 1 2 4 swaps this round: 3
#round 2  a: 1 2 3 4 swaps this round: 2
#round 3  a: 1 2 3 4 swaps this round: 0
#In the first round, the 4 is swapped at each of the 3 comparisons, 
#ending in the last position. In the second round, the 3 is swapped at 2 of the 3 comparisons.
#Finally, in the third round, no swaps are made so the iterations stop.
#The output is the following:

#Array is sorted in 5 swaps.
#First Element: 1
#Last Element: 4
#Input Format
#The first line contains an integer, n, the number of elements in array a.
#The second line contains n space-separated integers that describe a[0], a[1], . . .a[n – 1].

#Constraints
#2 <= n <= 600
#1 <= a[i] <= 2 x106, where 0 <= i < n
#Output Format
#Print the following three lines of output:

#Array is sorted in numSwaps swaps.
#where numSwaps is the number of swaps that took place.
#First Element: firstElement
#where firstElement is the first element in the sorted array.
#Last Element: lastElement
#where lastElement is the last element in the sorted array.
#Sample Input 0

#3
#1 2 3
#Sample Output 0

#Array is sorted in 0 swaps.
#First Element: 1
#Last Element: 3
##Explanation 0

#The array is already sorted, so 0 swaps take place and we print the necessary 3 lines of output shown above.

#Sample Input 1

#3
#3 2 1
#Sample Output 1

#Array is sorted in 3 swaps.
#First Element: 1
#Last Element: 3
#Explanation 1

#The array a = [3, 2, 1] is not sorted, so we perform the following 3 swaps. Each line shows a after each single element is swapped.


 
#[3, 2, 1] = [2, 3, 1]
#[2, 3, 1] = [2, 1, 3]
#[2, 1, 3] = [1 , 2, 3]
#After 3 swaps, the array is sorted.

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    j = 1
    i = 0
    swap = []
    # Write your code here
    for i in range(n):
        currentSwaps = 0
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap.append(a[i])
                currentSwaps += 1
        if currentSwaps == 0:
            break
          
    print("Array is sorted in",len(swap),"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])





