class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value

def preOrder(root):
    if root!= None:
        print("PreOrder: ",root.data, end=" -> ")

root=Node(1)
root.left=Node(3)
root.right=Node(5)
root.left.left=Node(2)
root.left.right=Node(4)
root.right.right=Node(8)
