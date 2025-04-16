# Class for adjacency list representation of data
import csv


class Graph:
    #-- Initialize the graph using the file
    def __init__(self, filename):
        self._adjList = {}
        self._numEdges = 0
        self._numNodes = 0
        self.loadGraph(filename)


    #-- Method to load the graph from the file
    def loadGraph(self, filename):
        nodes = set()
        
        # open file
        with open(filename) as file:
            reader = csv.reader(file, delimiter="\t")
            for row in reader:
                # skip comments at top of file
                if len(row) != 2: continue
                
                # get nodes
                nFrom, nTo = row
                nodes.add(nFrom)
                nodes.add(nTo)
                
                # add to adjacency list
                if nFrom not in self._adjList:
                    self._adjList[nFrom] = []
                self._adjList[nFrom].append(nTo)
                
                # increment number of edges
                self._numEdges += 1
        
        # set number of nodes
        self._numNodes = len(nodes)


    #-- Get the adjacent nodes
    def get_neighbors(self, node):
        return self._adjList.get(node, [])


    #-- Get the number of nodes in the graph
    def get_num_nodes(self):
        return self._numNodes


    #-- Get the number of edges in the graph
    def get_num_edges(self):
        return self._numEdges


    #-- Returns if two nodes have a direct path
    def has_edge(self, nFrom, nTo):
        return (nFrom in self._adjList) and (nTo in self._adjList[nFrom])


    #-- Gets the full adjacency list
    def get_adjList(self):
        return self._adjList