class Node:
    def __init__(self,value=None):
        self.prev=None
        self.next=None
        self.data=value

class doublyLL:
    def __init__(self,head=None):
        self.head=head
    
    def insertAtEnd(self,value):
        temp=Node(value)

        if self.head == None:
            self.head= temp
            return
        t=self.head
        while t.next != None:
            t.next=temp
            temp.prev=t

    def printLL(self):
        curr=self.head
        while curr.next != None:
            print(curr,end=" ")


        