class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value

def insert(root,value):
    if root == None:
        return Node(value)
    if root.data == value:
        return root
    if root.data > value:
        root.left.insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root
        