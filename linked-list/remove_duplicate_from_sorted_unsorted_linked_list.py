"""Given a linked list sorted in non-decreasing order. Return the list by deleting the duplicate nodes from the list.
The returned list should also be in non-decreasing order."""

# Input : Linked List = 11->11->11->21->43->43->60
# Output : 11->21->43->60

# Input : Linked List = 5->10->10->20
# Output : 5->10->20 (After removing duplicate elements)

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class SingleLinkedList:
    def __init__(self):
        self.head= None

    def display_all(self):
        data=[]
        if self.head is None:
            print("Linked list is empty")
            return data
        temp= self.head
        while temp:
            data.append(temp.data)
            temp= temp.next
        return data

    def remove_duplicate_from_sorted_ll(self):
        if self.head is None:
            return  # Empty list

        temp= self.head
        while temp.next:
            if temp.data==temp.next.data:
               # Skip the duplicate node
               temp.next= temp.next.next
            else:
                  # Only move forward if no duplicate found
                  temp= temp.next

    def remove_duplicate_from_unsorted_ll(self):
        if self.head is None:
            return
        seen= set()
        temp= self.head
        seen.add(temp.data)
        while temp.next:
            if temp.next.data in seen:
               # Skip the duplicate node
               temp.next= temp.next.next

            else:
                 # Only move forward if no duplicate found
                 seen.add(temp.next.data)
                 temp= temp.next


L=SingleLinkedList()
n1= Node(10)
L.head= n1
n2= Node(20)
n1.next= n2
n3= Node(30)
n2.next=n3
n4= Node(10)
n3.next= n4
n5= Node(5)
n4.next= n5
print(L.display_all())

L.remove_duplicate_from_unsorted_ll()

print(L.display_all())