class WeightedGraph:
    def __init__(self,vertices,edges):
        self.vertices=vertices
        self.edges=edges
        self.l=[]
        self.VTree=[]
        self.updatedEdges=[]
    def printVertices(self):
        pass
        
    def isAdjacentVertices(self,a,b):
        for x in edges:
            y=x[:-1]
            self.l.append(y)

        for i in range (len(self.l)):
            if [a,b] in self.l or [b,a] in self.l:
                return True
            else:
                return False
    
    def allPossibleEdges(self,vertex):
        

        ledges=[]
        
        for x in self.edges:
            if x[0]==vertex or x[1]==vertex:
                ledges.append(x)
        return ledges

    def comparePossibleEdges(self,vertex):
        ledges=self.allPossibleEdges(vertex)
        minWeight=ledges[0][2]
        index=0
        for l in ledges: #Compare their Weight
            for i in range(len(ledges)):
                if ledges[i][2]<minWeight:
                    minWeight=ledges[i][2]
                    index=i
         
        return ledges[index]
                        
    def remainingEdgesFromVertex(self,vertex):
        x=self.returnNextPossibleVertex(vertex)
        possibleVertexLessWeightEdge=self.comparePossibleEdges(x)
        list1=self.allPossibleEdges(vertex)
        list2=[]
        for i in range(len(list1)):
            
            if i not in self.comparePossibleEdges(vertex):
                list2.append(list1[i])
            
        return list2
        '''
        minWeight=list[0][2]
        index=i
        for i in range (len(list)):
            if list[i][2]<minWeight:
                minWeight=list[i][2]
                index=i
        return list[index]
        ''' 
        
    def remainingEdges(self,vertex):##Remaining Edges After a Vertex is considerd

        edgeConsidered = self.comparePossibleEdges(vertex)
        self.edges.remove(edgeConsidered)
        
        '''
        ## self.edges-self.consideredEdges
        getTheLeastWeightVertex.
        if vertex v is in self.vertexAdded Remove the considered Edge 
        '''
    def returnNextPossibleVertex(self,vertex):
        lessWeightEdge=self.comparePossibleEdges(vertex)
        
        if lessWeightEdge[0]==vertex:
            nextMoveVertex = lessWeightEdge[1]
        if lessWeightEdge[1]==vertex:
            nextMoveVertex = lessWeightEdge[0]

        return nextMoveVertex
        
    def isCycle(self):
        if self.returnNextPossibleVertex in self.VTree:
            return True

    def updatePossibleEdges(self,vertex):#update Possible edges after a vetex is considered
        pass     
        
        

 
    '''
        for i in range (len(self.vertices)-1):
            minimum=self.edges[0][2]
            if self.edges[i][2]<minimum:
                minimum=self.edges[i][2]
                index=i
            return self.edges[i]


    '''
edges=[[0,1,100],[0,2,3],[2,4,2],[2,3,40],[3,1,20],[4,3,5],[3,5,5],[5,4,9]]
vertex =[0,1,2,3,4,5]
x=WeightedGraph(vertex,edges)
root = vertex[0]

x.VTree.append(root)
while len(x.VTree)!=len(x.vertices):
    
    vertex=x.VTree[-1]
    x.updatedEdges.append(x.allPossibleEdges(vertex))
    
    
    
    x.VTree.append(x.returnNextPossibleVertex)

    
    

    




print("All Possible Moves")
print(str(x.allPossibleEdges(1))+ " For 1")
print(str(x.allPossibleEdges(2))+ " For 2")
print(str(x.allPossibleEdges(3))+ " For 3")
print(str(x.allPossibleEdges(4))+ " For 4")
print(str(x.allPossibleEdges(5))+ " For 5")

print("Compare Moves")
print(str(x.comparePossibleEdges(1))+ " For 1")
print(str(x.comparePossibleEdges(2))+ " For 2")
print(str(x.comparePossibleEdges(3))+ " For 3")
print(str(x.comparePossibleEdges(4))+ " For 4")
print(str(x.comparePossibleEdges(5))+ " For 5")



       

    
            
