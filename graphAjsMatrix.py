class Graph:
    def __init__(self,vertex):
        self.matrix =[[0]*vertex for _ in range(vertex)]
        self.size=vertex
    
    def add_edge(self,src,dest):
        if(0<=src<self.size and 0<=dest<self.size):
            self.matrix[src][dest]=1
            self.matrix[dest][src]=1  # For undirected graph    
        else:
            print("Invalid vertex") 

    def display(self):
        for row in self.matrix:
            print(" ".join(map(str,row)))

g=Graph(5)
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(3,4)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.display()


