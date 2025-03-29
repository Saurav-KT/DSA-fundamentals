from collections import deque
# Stack Implementation (LIFO - Last In, First Out)

"""Possible operations:
1. Add an item to the top of the stack
2. Remove and return the top item from the stack
3. Return the top item without removing it
4. Check if the stack is empty.
5. Return the number of items in the stack
"""
# Approach-1 stack implementation using list
# class Stack:
#     def __init__(self):
#         self.stack= []
#
#     def push(self, item):
#         """Add an item to the top of the stack."""
#         self.stack.append(item)
#
#     def pop(self):
#         """Remove and return the top item from the stack."""
#         return self.stack.pop() if not self.is_empty() else "stack is empty"
#
#
#     def pick_top_item(self):
#         """Return the top item without removing it."""
#         return self.stack[-1] if not self.is_empty() else "stack is empty"
#
#     def is_empty(self)->bool:
#         return len(self.stack)==0
#
#     def size(self)->int:
#         return len(self.stack)

# obj=Stack()
# obj.push(40)
# obj.push(50)
# obj.push(100)
# obj.push(10)
#
# print(obj.pop())
# print(obj.pick_top_item())
# print(obj.size())

# Approach-2 stack implementation using dequeue
class Stack:
    def __init__(self):
        self.stack= deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else "stack is empty"

    def is_empty(self)-> bool:
        return len(self.stack)==0

    def get_top(self):
        return self.stack[-1] if not self.is_empty() else "stack is empty"

    def size(self)-> int:
        return len(self.stack)


obj= Stack()
obj.push(10)
obj.push(30)
obj.push(48)
obj.push(200)
print(obj.pop())
print(obj.stack)
print(obj.size())
print(obj.get_top())