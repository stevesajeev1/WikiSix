# This file should have all the algorithms.
# Each algorithm should accept a graph object, start node and end node.

from collections import defaultdict
from collections import deque
from graph import Graph
import heapq

# Should return:
# - Number of nodes explored (visited list length)
# - Length/Degrees of the shortest path (optional, can just get from len(path))
# - A path array that includes all the shortest paths in a list of lists
#   * Example [["Florida", "x", "Wikipedia"], ["Florida", "y", "Wikipedia"]]
#   * The shortest paths are Florida -> x -> Wikipedia and Florida -> y -> Wikipedia


# Dijkstra Algorithm - Sriram
def dijkstra(graph: Graph, src, to):
    # get the number of nodes in the graph and initalize variables
    n = graph.get_num_nodes()
    INF = float('inf')
    dist = {node: INF for node in range(n)}    
    dist[src] = 0
    prev = defaultdict(list) # prev also holds paths

    # priority queue to hold (node, distance)
    pq = [(0, src)]

    # process until empty
    while pq:
        distance, node = heapq.heappop(pq)

        if distance > dist[node]:
            continue
        
        # relax all of node's edges
        for v in graph.get_neighbors(node):
            
            weight = 1 # unweighted so all edges w=1
            
            # node allows a smaller weight
            if dist.get(v, INF) > distance + weight:
                # replace the weight, append to pq, add to visited
                dist[v] = distance + weight
                prev[v] = [node]
                heapq.heappush(pq, (dist[v], v))
            
            elif distance+weight == dist[v]:
                prev[v].append(node) 

    # calculate the amount of nodes visited and the least distance
    visited = 0
    for d in dist.values():
        if d < INF: visited += d
    
    least_dist = dist[to] if dist.get(to, INF) < INF else None

    # now backtrack all the nodes for all shortest paths
    paths = []
    if (least_dist is not None):
        # stack with (node, path)
        stack = [(to, [])]
        while stack:
            node, path = stack.pop()
            if node == src:
                # reached end
                paths.append([src] + path)
            else:
                # add all previous
                for u in prev[node]:
                    stack.append((u, [node] + path))

    return visited, least_dist, paths


# breadth first search
def bfs(graph: Graph, src, to):
    # to keep track of nodes visited
    visited = set()
    # storing parent nodes
    parents = defaultdict(list)
    # BFS queue intialized
    queue = deque([src])
    distance = {src: 0}
    paths = []

    while queue:
        # FIFO
        node = queue.popleft()

        # checking all neighbors
        for neighbor in graph.get_neighbors(node):
            # if neighbor not visited then
            if neighbor not in distance:
                # set distance from src
                distance[neighbor] = distance[node] + 1
                # setting current node as parent
                parents[neighbor].append(node)
                queue.append(neighbor)
            elif distance[neighbor] == distance[node] + 1:
                # found another shortest path to neighbor
                parents[neighbor].append(node)

    # if not reachable
    if not distance:
        return len(distance), None, []

    # backtrack to build path all from to to src
    def backtrack(curr, path):
        if curr == src:
            # add completed path to list when source is reached
            paths.append([src] + path[::-1])
            return
        for p in parents[curr]:
            backtrack(p, path + [curr])

    # backtracking from destination node
    backtrack(to, [])

    return len(distance), distance[to], paths
    


# depth first search
def dfs(graph: Graph, src, to):
    pass


# Testing Code, example using Dijkstra
graph = Graph("backend/data/paths.tsv")
print(dijkstra(graph, "Florida", "Formula_One"))
print(bfs(graph, "Florida", "Formula_One"))
