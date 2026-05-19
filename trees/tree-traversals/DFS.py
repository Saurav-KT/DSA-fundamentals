
class TreeNode:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

# root, left, right
def pre_order(node, res):
    if not node:
        return

    # visit current node first
    res.append(node.data)
    pre_order(node.left,res)
    pre_order(node.right, res)

# left, root, right
def in_order(node, res):
    if not node:
        return

    in_order(node.left,res)

    # visit the current node
    res.append(node.data)
    in_order(node.right, res)

# left, right, root
def post_order(node, res):
    if not node:
        return
    post_order(node.left, res)
    post_order(node.right, res)

    # visit the current node
    res.append(node.data)

if __name__=="__main__":

    # pre order traversal

    # root= TreeNode(10)
    # root.left=TreeNode(20)
    # root.right=TreeNode(30)
    # root.left.left= TreeNode(40)
    # root.left.right= TreeNode(50)
    # root.right.left= TreeNode(60)
    # root.right.right= TreeNode(70)

    # result = []
    # pre_order(root, result)
    # print(*result)

    # in order traversal

    # root= TreeNode(10)
    # root.left=TreeNode(20)
    # root.right=TreeNode(30)
    # root.left.left= TreeNode(40)
    # root.left.right= TreeNode(50)
    # root.right.right= TreeNode(70)
    #
    # result=[]
    # in_order(root, result)
    # print(*result)

    # post order traversal
    root= TreeNode(1)
    root.left= TreeNode(2)
    root.right= TreeNode(3)
    root.left.left= TreeNode(4)
    root.left.right= TreeNode(5)
    root.right.right= TreeNode(6)

    result=[]
    post_order(root, result)
    print(result)




