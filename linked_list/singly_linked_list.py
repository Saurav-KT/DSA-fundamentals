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
          raise IndexError("Position cannot be negative")

        # Insert at the beginning if position is 0
        if position == 0:
            self.insert_at_beginning(data)
            return self.head

        # Cannot insert at a non-zero position in an empty list
        if self.head is None:
            raise IndexError("Position out of bound - list is empty")

        # Traverse to the node just before the target position
        temp= self.head
        for _ in range(1,position-1):
            if temp.next is None:
                raise IndexError("Position exceeds list length")
            temp= temp.next

        # Insert new node
        np = Node(data)
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

    def delete_at_beginning(self):
        """
           Deletes the first node (head) of the linked list.

           Returns:
               The data of the deleted node (if successful).

           Raises:
               IndexError: If the list is empty.
           """

        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        deleted_data= self.head.data # Store data before deletion
        # Case 1: Only one node (head.next is None)
        if self.head.next is None:
            self.head= None
        else:
            self.head = self.head.next

        return deleted_data

    def delete_at_end(self):
        """
                 Deletes the last node (tail) of the linked list.
                 Returns:
                     The deleted node's data if successful.
                 Raises:
                      IndexError: If the list is empty.
                 """
        # Case 1: Empty list → Raise error
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")

        # Case 2: Single-node list → Delete head
        if self.head.next is None:
            deleted_data= self.head.data
            self.head= None
            return deleted_data

        # Case 3: Multi-node list → Traverse to the second-last node
        temp= self.head.next
        prev= self.head
        while temp.next:
            temp= temp.next
            prev= prev.next
        deleted_data= temp.data
        prev.next= None
        return deleted_data

    def delete_at_position(self,position):
        """
        delete a new node with the given data at the specified position in the linked list.
        Args:
            position (int): The index where the specific node should be deleted (0-based).
            Raises:
            IndexError: If the position is negative, exceeds the list length, or the list is empty (for non-zero positions).
        """
        # Case 1: check negative position
        if position < 0:
            raise IndexError("Position cannot be negative")

        # Case 2: Empty list
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")

        deleted_data = None

        # Case 3: Delete head node (handles both single-node and multi-node cases)
        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data

        # Case 4: Traverse to the node before the target position
        prev = None
        current = self.head
        current_pos = 0

        while current is not None and current_pos < position:
            prev = current
            current = current.next
            current_pos += 1

        # If position exceeds list length
        if current is None:
            raise IndexError("Position exceeds list length")

        # Delete the node at the target position

        prev.next= current.next
        return deleted_data

    def delete_by_specific_value(self, value):

        #  Case 1: Empty list
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")

        # Case 2: Delete head node (handles both single-node and multi-node cases)
        if self.head.data==value:
            deleted_data= self.head.data
            self.head= self.head.next
            return deleted_data

        # Case 4:  # Traverse the list to find the node with the target value
        current = self.head
        prev= None
        while current:
            if current.data == value:
                deleted_data= current.data
                # Adjust the pointers to skip the node with the target value
                prev.next = current.next
                return deleted_data

            prev = current
            current = current.next

            # Value not found
        raise ValueError(f"Value {value} not found in the list")

    def update_the_value_at_specific_position(self,position,value):
        # Case 1: check negative position
        if position < 0:
            raise IndexError("Position cannot be negative")

        # Case 2: Empty list
        if self.head is None:
            raise IndexError("Cannot update an empty list")


        # Case 3: Update head node (handles both single-node and multi-node cases)
        if position == 0:
            updated_data = self.head.data
            self.head.data = value
            return updated_data

        # Case 4: Traverse to the node before the target position
        current = self.head
        current_pos = 0
        while current is not None and current_pos < position:
            current = current.next
            current_pos += 1

        # If position exceeds list length
        if current is None:
            raise IndexError("Position exceeds list length")

        updated_data= current.data
        current.data= value
        return updated_data


L= SingleLinkedList()
n1= Node(10)
L.head= n1
n2= Node(20)
L.head.next= n2
n1.next=n2
n3= Node(30)
n2.next= n3
n4= Node(40)
n3.next= n4
L.update_the_value_at_specific_position(2,100)
print(L.display_all())
# L.insert_at_beginning(50)
# delete_data = L.delete_at_end()
# print(delete_data)
# print(L.display_all())
# print(L.delete_by_specific_value(100))
# print(L.delete_at_position(6))
# print(L.display_all())

# L.delete_at_end()
# print(L.display_all())
# L.delete_at_beginning()
# print(L.display_all())



# L.insert_at_beginning(5)
# L.insert_at_beginning(3)
# L.insert_at_end(80)
# L.insert_at_end(100)
# L.insert_at_specific_position(-1,25)
# L.insert_at_specific_position(10,35)
# print(L.display_all())



