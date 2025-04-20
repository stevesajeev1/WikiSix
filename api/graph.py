# Class for adjacency list representation of data
import csv
from urllib.parse import unquote


class Graph:
    #-- Initialize the graph using the file
    def __init__(self, filename):
        self._adjList = {}
        self.loadGraph(filename)


    #-- Method to load the graph from the file
    def loadGraph(self, filename):
        # open file
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter="\t")
            for row in reader:
                # skip comments at top of file
                if len(row) != 2: continue
                
                # get nodes
                nFrom, nTo = row
                nFrom = unquote(nFrom).lower()
                nTo = unquote(nTo).lower()
                
                # add to adjacency list
                if nFrom not in self._adjList:
                    self._adjList[nFrom] = []
                self._adjList[nFrom].append(nTo)


    #-- Get the adjacent nodes
    def get_neighbors(self, node):
        return self._adjList.get(node, [])


    #-- Returns if node in graph
    def hasNode(self, node):
        return node in self._adjList