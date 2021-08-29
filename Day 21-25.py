#Day 21:                                Generics



#Objective
#Today we’re discussing Generics; be aware that not all languages support this construct, 
#so fewer languages are enabled for this challenge.

#Task
#Write a single generic function named printArray;
#this function must take an array of generic elements as a parameter 
##(the exception to this is C++, which takes a vector). 

#The locked Solution class in your editor tests your function.

#Note: You must use generics to solve this challenge. Do not write overloaded functions.

#Input Format
#The locked Solution class in your editor will pass different types of arrays to your printArray function.

#Constraints
#You must have exactly 1 function named printArray.
#Output Format
#Your printArray function should print each element of its generic array parameter on a new line.


#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <class T> 
    void printArray(vector<T> i) 
 { 
    for(int j=0;j<i.size();j++) 
        cout<<i[j]<<endl;
 } 

int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}


#Day22                               Binary Search Tree


#Task
#The height of a binary search tree is the number of edges between the tree’s root and its furthest leaf.
#You are given a pointer, root, pointing to the root of a binary search tree. 
#Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

#Input Format
#The locked stub code in your editor reads the following inputs and assembles them into a binary search tree:
#The first line contains an integer, n, denoting the number of nodes in the tree.
#Each of the n subsequent lines contains an integer, data, denoting the value of an element that must be added to the BST.

#Output Format
#The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

#Sample Input


 
#7
#3
#5
#2
#1
#4
#6
#7
#Sample Output

#3
#Explanation

#There are 4 nodes in this path that are connected by 3 edges, meaning our BST’s height = 3. 
#Thus, we print 3 as our answer.


class Node:
    def __init__(self,data):                    #constructor
        self.right=self.left=None
        self.data = data
class Solution:                                 #insert in BST function
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):                                 #to get height of tree
        #Write your code here
        if root == None or root.left == root.right == None:
            return 0 
        else:
            return 1+ max(self.getHeight(root.left),
                           self.getHeight(root.right))
                           

T=int(input())                                                #main
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       


