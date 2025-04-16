# This file should have all the algorithms.
# Each algorithm should accept a graph object, start node and end node.

from graph import Graph
import heapq

# Should return:
# - Number of nodes explored (visited list length)
# - Length/Degrees of the shortest path (optional, can just get from len(path))
# - A path array that includes path eg. ['Florida', 'Greenland', 'Tin'] is Florida -> Greenland -> Tin

# Testing Code, example using Dijkstra
# graph = Graph("backend/data/paths.tsv")
# print(dijkstra(graph, "Florida", "Wikipedia")) # prints (4053, 3, ['Florida', 'English_language', 'HTTP_cookie', 'Wikipedia'])



# Dijkstra Algorithm - Sriram
def dijkstra(graph: Graph, src, to):
    # get the number of nodes in the graph
    n = graph.get_num_nodes()

    # initialize the distances and previous
    INF = float('inf')
    dist = {node: INF for node in range(n)}
    dist[src] = 0
    prev = {node: -1 for node in range(n)}
    prev[src] = 0

    # initialize visited set
    visited = set()

    # priority queue to hold (node, distance)
    pq = [(src, 0)]

    # process until empty
    while pq:
        node, distance = heapq.heappop(pq)

        # check if node already visited
        if node in visited:
            continue
        
        # add to visited nodes
        visited.add(node)

        # relax all of node's edges
        for v in graph.get_neighbors(node):
            
            if v not in dist:
                dist[v] = INF
            
            if v not in prev:
                prev[v] = -1
            
            weight = 1
            # node allows a smaller weight and v is not visited
            if dist[v] > distance + weight:
                # replace the weight, append to pq, add to visited
                dist[v] = distance + weight
                prev[v] = node
                heapq.heappush(pq, (v, dist[v]))
            
            if v == to:
                # found the destination (to) node
                break

    # append the path
    path = []
    current_node = to
    while prev[current_node] != 0 and dist[current_node] != INF:
        path.append(current_node)
        current_node = prev[current_node]

    path.append(src)

    path.reverse()

    return len(visited), dist[to] if to in dist else INF, path


# breadth first search
def bfs(graph: Graph, src, to):
    pass


# depth first search
def dfs(graph: Graph, src, to):
    pass