class Node(object):
    def __init__(self,data):
        self.data= data
        self.next= None

class Stack(object):
    def __init__(self):
        self.top= None
        self._size=0

    def push(self, data):
        new = Node(data)
        if self.is_empty():
            self.top=new
            self.top.next=None
        else:
            new.next=self.top
            self.top=new
        self._size+=1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        elif self.top.next is None:
            print("Popped element is:", self.top.data)
            print("------------------------------")
            popped_data = self.top.data
            self.top= None
        else:
            temp= self.top
            print("Popped element is:", self.top.data)
            print("------------------------------")
            popped_data = self.top.data
            self.top= temp.next
            temp= None
        self._size-=1
        return popped_data


    def display(self):
        # Print all elements in the stack.
        if self.is_empty():
            print("Stack is Empty")
            print("--------------------")
            return
        print("Elements of the stack are")
        temp= self.top
        while temp:
            print(temp.data)
            temp= temp.next
        print("-------------------------------------")

    def is_empty(self)->bool:
        return self.top is None

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def size(self):
      return self._size

#
# s= Stack()
# s.push(20)
# s.push(30)
# s.display()
# print("Top item of the stack",s.pick_top_item())
# print("total count",s.size())




