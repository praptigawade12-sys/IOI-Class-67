class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[0]*vertices for i in range(vertices)]

    def add_edge(self,u,v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def display(self):
        for i in self.graph:
            print(i)

g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.display()