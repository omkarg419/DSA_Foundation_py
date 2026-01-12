class Deque:
    def __init__(self):
        self.item=[]
    
    def isEmpty(self):
        return len(self.item) == 0

    def insertATEnd(self,value):
        self.item.append(value)
    
    def insertAtBeg(self,value):
        self.item.insert(0,value)