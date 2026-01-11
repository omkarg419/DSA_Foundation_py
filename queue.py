class Queue:
    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return len(self.item) == 0
    
    def insert(self,value):
        self.item.append(value)
    
    def delete(self):
        if self.isEmpty() :
            print("Queue is empty")
        else:
            return self.item.pop(0)    


        