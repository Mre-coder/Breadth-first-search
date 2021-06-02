from collections import defaultdict

 

 

class BFS:

    numofelements = 0

    graph = defaultdict(list)

    def init(self):

        self.graph = defaultdict(list)

 

   

    def addNode(self, node, newnode):

        self.numofelements = self.numofelements + 1

        self.graph[node].append(newnode)

 

 

    def traverseBFS(self, currentnode):

        graphlen = self.numofelements + 1

        VisitedNodes = [False] * graphlen

        BFSQueueNodes = []

       

        BFSQueueNodes.append(currentnode)

        VisitedNodes[currentnode-1] = True

        #print(VisitedNodes)

       

        while BFSQueueNodes:

            currentnode = BFSQueueNodes.pop(0)

            print("{} ".format(currentnode))

           

            for node in self.graph[currentnode]:

                #print(" Node is {}".format(node))

                if (VisitedNodes[node-1] == False):

                    BFSQueueNodes.append(node)

                    VisitedNodes[node-1] = True

 

 

def AddNodes(g1):

    g1.addNode(1, 2)

    g1.addNode(1, 3)

    g1.addNode(2, 4)

    g1.addNode(2, 5)

    g1.addNode(2, 6)

    g1.addNode(3, 7)

    g1.addNode(7, 8)

    g1.addNode(7, 9)

    return g1

   

    

def GetNodes(g1):

    n = int(input("Enter num of Edges : "))

    for i in range(0,n):

        f = int(input("Enter from : "))

        t = int(input("Enter to   : "))

        g1.addNode(f,t)

    return g1

 

       

graph1 = BFS()

 

 

graph1 = GetNodes(graph1)

print(graph1.graph)

 

s = int(input("Enter start node: "))

graph1.traverseBFS(s)
