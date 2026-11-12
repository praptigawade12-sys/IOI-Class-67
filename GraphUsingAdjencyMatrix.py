class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,u,v):
        self.graph.setdefault(u,[]).append(v)
        self.graph.setdefault(v,[]).append(u)

    def display(self):
        for i in self.graph:
            print(i,self.graph[i])

g = Graph()

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,6)

g.display()