class Deque:
    def __init__(self):
        self.item=[]
    
    def isEmpty(self):
        return len(self.item) == 0

    def insertATEnd(self,value):
        self.item.append(value)
    
    def insertAtBeg(self,value):
        self.item.insert(0,value)
    
    def deleteATFornt(self):
        if(self.isEmpty()):
            print(" Deque is empty")
        else:
            return self.item.pop(0)
    
    def deleteAtReare(self):
        if(self.isEmpty()):
            print(" Deque is empty")
        else:
            return self.item.pop()
        
D=Deque()
D.insertATEnd(10)
D.insertATEnd(20)
D.insertAtBeg(30)
D.insertAtBeg(40)

print(D.deleteATFornt())