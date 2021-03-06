# Adjacency List implementation
#Undirected graph
class Graph:
    def __init__(self):

        self.edges={}


    def addVertex(self,v):

        if v not in self.edges:
            self.edges[v]=[]


    def addEdge(self,from_v,to_v):

        if from_v not in self.edges:
            self.edges[from_v]
        if to_v not in self.edges:
            self.edges[to_v]=[]

        if to_v not in self.edges[from_v]:
            self.edges[from_v].append(to_v)
        if from_v not in self.edges(to_v):
            self.edges[to_v].append(from_v)

    def isEdge(self,from_v,to_v):
        #determines whether edge exists

        if to_v not in self.edges:
            return False
        if from_v not in self.edges:
            return False
        
        return to_v in self.edges[from_v]




simple = { 1:[2,3,5],
           2:[1,4],
           3:[1],
           4:[2,5],
           5:[1,4] }



def loadGraph(edges):
    '''Create a graph instance'''

    g=Graph()
    for v in edges:
        g.addVertex(v)
        for neighbor in edges[v]:
            g.addEdge(v,neighbor)

    return g



White=0
Gray=1
Black=2
class DepthFirstTraversal:
    def __init__(self,graph,s):

        self.graph=graph
        self.start=s
        self.color={}
        self.pred={}

        for v in graph.edges:
            self.color[v]=White
            self.pred[v]=None

        self.dfs_visit(s)

    def dfs_visit(self,u):
        #Recurisve Traversal or graph using dfs

        self.color[u]=Gray

        for v in self.graph.edges[u]:
            if self.color[v] is White:
                self.pred[v]=u
                self.dfs_visit(v)
        

        
        self.color[u]=Black


    def solution(self,v):
        #Recover path from start to this vertex

        if v is not in self.graph.edges:
            return None
        if self.pred[v] is None:
            return None

        path=[v]

        while v!= self.start:
            v=self.pred[v]
            path.insert(0,v)



        return path
