class stack:

    def __init__(self):
        self.s=[]

    def Length(self):
        return len(self.s)
    
    def Push(self,value):
        # self.s.insert(0,value)
        self.s.append(value)

    def Peek(self):
        if len(self.s) == 0:
            raise Exception("Empty Stack")
        else:
            # return self.s[0]
            return self.s[-1]
    
    def Pop(self):
         if len(self.s) == 0:
            raise Exception("Empty Stack")
         else:
            return self.s.pop(0)
            # return self.s.pop()
         

stk =stack()

stk.Push(10)
stk.Push(20)
stk.Push(30)
stk.Push(40)
stk.Push(50)

print("peek element: ",stk.Peek())
print("pop element: ",stk.Pop())
print("pop element: ",stk.Pop())
print("peek element: ",stk.Peek())
print("Length of Stack: ",stk.Length())