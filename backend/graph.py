# Class for adjacency list reprsentation of data
# TODO: include a text file that just has the connections between sites

class Graph:

#-- Initialize the graph using the file
    def __init__(self, filename):
        self._adjList = {}
        self._numEdges = 0
        self._numNodes = 0
        self.loadGraph(filename)


#-- Method to load the graph from the file
    def loadGraph(self, filename):
        # open the file for reading
        file = open(filename, 'r')

        # read each line and connect the approiate nodes
        for line in file:
            # initialize the from and to nodes
            nFrom, nTo = line.split()

            # add nodes into adjacency list if not
            if nFrom not in self._adjList:
                self._adjList[nFrom] = []
            if nTo not in self._adjList:
                self._adjList[nTo] = []

            # add the edge (nFrom -> nTo)
            self._adjList[nFrom].append(nTo)

            # increment the number of edges
            self._numEdges += 1
        
        # update number of nodes/vertices
        self._numNodes = len(self._adjList)


#-- Get the adjacent nodes
    def get_neighbors(self, node):
        # check if node is in adj list
        if (node not in self._adjList):
            return []
        # if is, return [] of neighs
        return self._adjList[node]


#-- Get the number of nodes in the graph
    def get_num_nodes(self):
        return self._numNodes


#-- Returns if two nodes have a direct path
    def has_edge(self, nFrom, nTo):
        if nFrom in self._adjList:
            if nTo in self._adjList[nFrom]:
                return True
        return False
    

#-- Gets the full adjacency list
    def get_adjList(self):
        return self._adjList

