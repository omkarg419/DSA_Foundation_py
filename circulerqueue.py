class CirculerQueue:
    
    def __init__(self,size):
        self.size= size
        self.item=[None]*size
        self.front=self.rear=-1
    
    def enqueue(self,value):
        if((self.rear + 1) == self.front):
            print("Queue is Full")
        elif self.front == -1:
            self.front=self.rear=0
            self.item[self.rear]=value
        else:
            self.rear=(self.rear +1) % self.size
            self.item[self.rear]=value

    def dequeue(self):

        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            print(self.item[self.front])
            self.front=self.rear=-1
        else:
            print(self.item[self.front])
            self.front=(self.front +1) % self.size

CQ=CirculerQueue()

CQ.enqueue(10)
CQ.enqueue(20)
CQ.enqueue(30)
CQ.enqueue(40)

   


