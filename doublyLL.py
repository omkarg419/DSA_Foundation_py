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
            t= t.next

        t.next=temp
        temp.prev=t

    def insertionAtBegn(self,value):
        temp=Node(value)

        self.head.prev=temp
        temp.next=self.head
        self.head=temp

    def printLL(self):
        curr=self.head
        while curr.next != None:
            print(curr.data,end=" <--> ")
            curr=curr.next
        print(curr.data)    
        

obj=doublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertionAtBegn(5)
obj.printLL()
        