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
        
    def insert_at_middle(self,value, x):
        temp=Node(value) 
        t1=self.head

        while(t1.next != None):
            if(t1.data == x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next
           
    def deleteLL(self,value):
        t1=self.head
        prev=t1
        if(t1.data == value):
            self.head=t1.next
        while(t1.next != None):
            if(t1.data == value):
                prev.next=t1.next
                break
            else:
                prev=t1
                t1=t1.next
        if(t1.data == value):
            prev.next=None
            
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
obj.insert_at_middle(800,300)
obj.deleteLL(400)
obj.printLL()
        