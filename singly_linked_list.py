class Node:
    def __init__(self, data):
        # Automatically assign data
        self.data = data
        # Initialize next pointer as null
        self.next = None


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def print_data(self):
        val = self.head
        while val:
            print(val.data, end=" ")
            val = val.next

    # Add new node at the beginning
    def add_at_begining(self, newdata):
        # Allocate the Node & Put in the data
        new_node = Node(newdata)
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node

    # Add a node at the end
    # Create a new node. Put in the data
    def add_at_end(self, newdata):
        new_node = Node(newdata)
        # If the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # Change the next of last node
        last.next = new_node

    # This method inserts a new node after a given prev_data
    def insertAfter(self, prev_data, new_data):
        # 1. check if the Linked List is empty or not
        if self.head is None:
            return
        # 2. Create new node & Put in the data
        new_node = Node(new_data)

        # 3. If prev_data is at the first position
        if prev_data == self.head.data:
            new_node.next = self.head.next
            self.head.next = new_node
            return
        # 4. check if the given prev_data exists
        head = self.head
        while head.data != prev_data:
            head = head.next
            if head is None:
                return
        new_node.next = head.next
        head.next = new_node


# Start with the empty list
list1 = LinkedList()

# Insert 6.  So linked list becomes 6->None
list1.add_at_end(6)

# Insert 7 at the beginning. So linked list becomes 7->6->None
list1.add_at_begining(7)

# Insert 1 at the beginning. So linked list becomes 1->7->6->None
list1.add_at_begining(1)

# Insert 4 at the end. So linked list becomes 1->7->6->10->None
list1.add_at_end(10)

list1.insertAfter(6,99)
list1.insertAfter(99,203)
list1.print_data()
# list1.head = Node("Mon")
# n2 = Node("Tue")
# n3 = Node("Wed")
# n4 = Node("Thu")

# Link first Node to second node
# list1.head.next = n2

# Link second Node to third node
# n2.next = n3

# Link second Node to fourth node
# n3.next = n4

# list1.at_begining("Sun")
# list1.print_data()
