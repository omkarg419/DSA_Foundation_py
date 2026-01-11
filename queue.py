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


Q=Queue()

Q.insert(10)
Q.insert(20)
Q.insert(30)
Q.insert(40)

print(Q.delete())
print(Q.delete())
print(Q.delete())
print(Q.delete())
print(Q.delete())

        