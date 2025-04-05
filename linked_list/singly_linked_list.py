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

    def insert_at_beginning(self,data):
        if data is None:
            return None

        nb= Node(data)
        nb.next=self.head
        self.head= nb
        return nb

    def insert_at_end(self,data):
        if data is None:
            return None
        ne= Node(data)
        if self.head is None:
            self.head= ne
            return ne

        temp= self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        return ne

    def insert_at_specific_position(self,position,data):
        """
            Inserts a new node with the given data at the specified position in the linked list.

            Args:
                position (int): The index where the new node should be inserted (0-based).
                data: The data to be stored in the new node.

            Raises:
                IndexError: If the position is negative, exceeds the list length, or the list is empty (for non-zero positions).
            """

        # Check for invalid negative position

        if position < 0:
          raise IndexError("Position out of bound")

        # Insert at the beginning if position is 0
        if position == 0:
            self.insert_at_beginning(data)
            return

        # Cannot insert at a non-zero position in an empty list
        if self.head is None:
            raise IndexError("Position out of bound - list is empty")

        # Traverse to the node just before the target position
        temp= self.head
        for _ in range(1,position-1):
            if temp is None:
                break
            temp= temp.next

        # if position is greater number of nodes
        if temp is None:
            raise IndexError("Position out of bound")

        # Create and insert the new node
        np = Node(data)
        np.data= data
        np.next= temp.next
        temp.next= np
        return self.head

    def search_element(self, data):
        if data is None:
            return None
        temp= self.head
        while temp:
            if temp.data== data:
                return temp.data
            temp= temp.next
        return None

    def display_all(self):
            data = []
            if self.head is None:
                print("Linked list is empty")
                return data
            else:
                temp= self.head
                while temp:
                    data.append(temp.data)
                    # print(temp.data, "-->",end=" ")
                    temp= temp.next
                return data





# L= SingleLinkedList()
# n= Node(10)
# L.head= n
# n1= Node(20)
# # L.head.next= n1
# n.next=n1
# n2= Node(30)
# n1.next= n2
# n3= Node(40)
# n2.next= n3
# n4= Node(50)
# n3.next= n4


# L.insert_at_beginning(5)
# L.insert_at_beginning(3)
# L.insert_at_end(80)
# L.insert_at_end(100)
# L.insert_at_specific_position(4,25)
# L.insert_at_specific_position(10,35)
# print(L.display_all())



