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
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root

def search(root,value):
    if root == None:
        print("element not found: ",value, end="\n")
        return
    if root.data == value:
        print("Element found: ",root.data ,end="\n")
        return
    if root.data > value:
        search(root.left,value)
    else:
        search(root.right,value)

def delete(root,value):
    if root == None:
        return root
    if root.data>value:
        root.left=delete(root.left,value)
    if root.data<value:
        root.right=delete(root.right,value)

    else:
        if(root.left == None):
            return root.right
        if root.right == None:
            return root.left    
        
def InOrder(root):
    if root != None:    
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)

root=insert(None,20)
root=insert(root,30)
root=insert(root,10)
root=insert(root,15)
root=insert(root,50)
root=insert(root,90)
root=insert(root,18)

InOrder(root)
search(root,90)
search(root,5)