#Task11
# Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and
# an instructional video!

# Context 
# Given a 6 x 6 2D Array, A:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

# Task 
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

# Input Format
# There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A will be in the
# inclusive range of -9 to 9.

# Constraints
# -9 <= A[i][j] <= 9
# 0 <= i,j <= 5

# Output Format
# Print the largest (maximum) hourglass sum found in A.
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
          
    sum1=[]
    
    for x in range (4):
        for y in range (4):
             s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
             sum1.append(s)
    
    print (max(sum1))
    
    
#Task 12 inheritance

You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Studentinherits all the properties of Person.

Complete the Student class by writing the following:

    A Student class constructor, which has  parameters:
        A string, .
        A string, .
        An integer, .
        An integer array (or vector) of test scores, .
    A char calculate() method that calculates a Student object’s average and returns the grade character representative of their calculated average:

Sample Input
Heraldo Memelli 8135627
2
100 80
	
Heraldo Memelli 8135627
2
100 80

Sample Output
Name: Memelli, Heraldo
ID: 8135627
Grade: O

	
Name: Memelli, Heraldo
ID: 8135627
Grade: O







class Person:
	def __init__(self, firstName, lastName, idNumber):		#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, fname, lname, idnum, scr):
        super().__init__(fname, lname, idnum)        		#super() function that will make the child class inherit all the methods and properties from its parent:
        self.scores = scr                                       #since score was not declared in parent class

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):

        scoresum = 0
        for i in range (numScores):
            scoresum = scores[i] + scoresum				#sum all scores
            
        average = scoresum/numScores
        
        if average <=100 and average >=90:
            return("O")
        elif average <90 and average >=80:
            return("E")
        elif average <80 and average >=70:
            return("A")
        elif average <70 and average >=55:
            return("P")
        elif average <55 and average >=40:
            return("D")
        elif average <40 :
            return("T")
        else :
            return ("invalid")
            
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())






#task 13
#The objective of this day is to make us aware of the basic implementation of the abstract classes:
	Task 
	Given a Book class and a Solution class, write a MyBook class that does the following:
   	. Inherits from Book
   	.  Has a parameterized constructor taking these  parameters:
       		 string 
       		 string 
        	 int 
  	 . Implements the Book class’ abstract display() method so it prints these  lines:
        	Title, a space, and then the current instance’s .title
        	Author, a space, and then the current instance’s .author
        	Price, a space, and then the current instance’s .price







from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
        
#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)			#import the objects from parent class
        self.price = price				#price object declared
        
    def display(self):
        print ("Title: " + self.title)
        print ("Author: " + self.author)
        print ("Price: " + str(price))			#no self needed bcz obj created in this class rather than parent class
        
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()



#DAy 14

#Objective

Today we’re discussing scope. Check out the Tutorial tab for learning materials and an instructional video!
The absolute difference between two integers, a and b, is written as |a - b|. The maximum absolute difference between two integers in a set of positive integers, elements, is the largest absolute difference between any two integers in elements.
The Difference class is started for you in the editor. It has a private integer array (elements) for storing N non-negative integers, and a public integer (maximumDifference) for storing the maximum absolute difference.

Task

Complete the Difference class by writing the following:
    . A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
    . A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference instance variable.

Input Format

You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in 2 lines of input; the first line contains N, and the second line describes the elements array.
Constraints
    1 <= N <= 10
    1 <= elements[i] <= 100, where 0 <= i <= N - 1

Output Format

You are not responsible for printing any output; the Solution class will print the value of the maximumDifference instance variable.
Sample Input	

3
1 2 5

Sample Output

4

Explanation

The scope of the elements array and maximumDifference integer is the entire class instance. The class constructor saves the argument passed to the constructor as the elements instance variable (where the computeDifference method can access it).
To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference between any 2 elements: |1 - 2| = 1
|1 - 5| = 4
|2 - 5| = 3
The maximum of these differences is 4, so it saves the value 4 as the maximumDifference instance variable. The locked stub code in the editor then prints the value stored as maximumDifference, which is 4.





class Difference:
    def __init__(self, a):
        self.__elements = a
# Add your code here
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)
            

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)


#DAy 15

#inserting elements at the end of a linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method 
        temp = Node(data)
        if head is None:
            head = temp
            return head
        current = head
        while current.next is not None:
            current = current.next
        current.next = temp
        return head      
                        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
 

