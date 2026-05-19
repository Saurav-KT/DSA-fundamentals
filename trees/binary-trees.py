# Binary tree representation

class TreeNode:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

root= TreeNode(10)
root.left= TreeNode(5)
root.right= TreeNode(10)
root.left.left= TreeNode(2)
root.right.right= TreeNode(7)



