# This file should have all the algorithms.
# Each algorithm should accept a graph object, start node and end node.
# It should return the number of nodes explored and ALL the shortest paths.

# Imports
from graph import Graph
import heapq


# Algorithm Functions
# Should take in src, to
# Should output number of nodes explored and shortest path

# Dijkstra Algorithm - not working rn
def dijkstra(graph:Graph, src, to):

    # get the number of nodes in the graph
    n = graph.get_num_nodes()

    # initialize the distances
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0

    # initialize visited set
    visited = set()

    # priority queue to hold (node, distance)
    pq = [(src, 0)]

    # process until empty
    while pq:
        node = heapq.heappop(pq)

        # relax all of node's edges
        for v in graph.get_neighbors(node):
            weight = 1
            # node allows a smaller weight and v is not visited
            if (dist[v] > dist[node] + weight) & (v not in visited) :
                # replace the weight, append to pq, add to visited
                dist[v] = dist[node] + weight
                pq.append((v,weight))
                visited.add(v)
            
                if v is to:
                    # found the destination (to) node
                    break
    
    return len(visited), dist[to]


# breadth first search
def bfs (graph:Graph, src, to):
    pass


# depth first search
def dfs (graph:Graph, src, to):
    pass
