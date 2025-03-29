"""
Link list basic operations
Traversal: Visit each node in the list to access or process its data.
Insertion: Insert a node at the beginning of the list.
Insert a node at the end of the list.
Insert a node at a specific position in the list.

Deletion:
Delete a node from the beginning of the list.
Delete a node from the end of the list.
Delete a node from a specific position in the list.
Delete a node with a specific value.

Searching
Search for a node with a specific value.
Check if a value exists in the list.

Updating
Update the value of a node at a specific position.

Length Calculation
Count the number of nodes in the list.
"""

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None # Address of next node

class SingleLinkedList:
    def __init__(self):
        self.head= None

    def insert_at_begining(self,data):
        if data is None:
            raise "Value can't be None"

        nb= Node(data)
        nb.next=self.head
        self.head= nb

    def insert_at_end(self,data):
        ne= Node(data)
        temp= self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    def insert_at_specific_position(self,position,data):
        if position ==0:
            self.insert_at_begining(data)

        np= Node(data)
        temp= self.head
        for i in range(position-1):
            if temp is None:
                raise IndexError("Position out of bound")
            temp= temp.next
        np.data= data
        np.next= temp.next
        temp.next= np

    def display(self):
            if self.head is None:
                print("Linked list is empty")
            else:
                temp= self.head
                while temp:
                    print(temp.data, "-->",end=" ")
                    temp= temp.next


L= SingleLinkedList()
n= Node(10)
L.head= n
n1= Node(20)
# L.head.next= n1
n.next=n1
n2= Node(30)
n1.next= n2
n3= Node(40)
n2.next= n3
n4= Node(50)
n3.next= n4
# Display data

L.insert_at_begining(5)
L.insert_at_begining(3)
L.insert_at_end(80)
L.insert_at_end(100)
L.insert_at_specific_position(4,25)
L.insert_at_specific_position(10,35)
L.display()



