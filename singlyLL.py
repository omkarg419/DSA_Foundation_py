class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
        

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head

    def insert_at_End(self,value):
        temp= Node(value)
        if (self.head != None):
           t1=self.head
           while(t1.next != None):
                t1=t1.next
           t1.next=temp 
        else:
            self.head=temp 

    def insert_at_start(self,value):
        temp=Node(value)
        
        temp.next=self.head
        self.head=temp
        
    def 

    def printLL(self):
        
        curr=self.head
        while(curr.next != None):
            print(curr.data)
            curr=curr.next
        print(curr.data)                 
           
obj = SinglyLinkedList()
obj.insert_at_End(100)
obj.insert_at_End(300)
obj.insert_at_End(600)
obj.insert_at_start(400)
obj.printLL()
        