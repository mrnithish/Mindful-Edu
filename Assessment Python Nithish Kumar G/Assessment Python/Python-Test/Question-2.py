"""
Given two linked list insert nodes of second list into first list
at alternate positions of first list.
For example, if first list is 5->7->17->13->11
and second is 12->10->2->4->6, the first list should
become 5->12->7->10->17->2->13->4->11->6 and
second list should become empty. So, for this question first make two
lists list1 and list2. Then in output merge them.

Input: list1: 3->7->9 , list2: 8->12
Output: 3->8->7->12->9

Input: list1: 5->9, list2: 4->11->15
Output: 5->4->9->11->15
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtBegin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insertAtEnd(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            node=self.head
            while node.next is not None:
                node=node.next
            node.next=newnode
            
    def display(self):
        node=self.head
        if node is None:
            print("Empty")
        else:
            while node :
                print(node.data,end=" -> ")
                node=node.next
            print()

    def mergeL(self,list1,list2):
        while (list1.head is not None) or (list2.head is not None):
            if list1.head is not None:
                self.insertAtEnd(list1.head.data)
                list1.head=list1.head.next
            if list2.head is not None:
                self.insertAtEnd(list2.head.data)
                list2.head=list2.head.next
        
            

list1=LinkedList()
list2=LinkedList()
list1.insertAtEnd(3)
list1.insertAtEnd(7)
list1.insertAtEnd(9)
list1.display()

list2.insertAtEnd(8)
list2.insertAtEnd(12)
list2.display()

o=LinkedList()
o.mergeL(list1,list2)
o.display()      
        
