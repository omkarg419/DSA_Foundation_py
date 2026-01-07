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

        if self.head == None:
            self.head= temp
            return
        
        self.head.prev=temp
        temp.next=self.head
        self.head=temp

    def insertAtMiddle(self,value,x):
        temp=Node(value)
        t1=self.head
        while t1.next != None:
            if t1.data == x:
                break
            else:
                t1=t1.next
        temp.next=t1.next
        t1.next.prev=temp
        t1.next=temp
        temp.prev=t1

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
obj.insertAtMiddle(50,20)
obj.printLL()
        