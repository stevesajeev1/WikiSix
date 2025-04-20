# This file should have all the algorithms.
# Each algorithm should accept a graph object, start node and end node.

from collections import defaultdict
from collections import deque
import heapq
from .graph import Graph

# Should return:
# - Number of edges explored
# - Length/Degrees of the shortest path
# - A path array that includes all the shortest paths in a list of lists
#   * Example [["florida", "x", "wikipedia"], ["florida", "y", "wikipedia"]]
#   * The shortest paths are florida -> x -> wikipedia and florida -> y -> wikipedia


# Dijkstra Algorithm - Sriram
def dijkstra(graph: Graph, src, to):
    # initialize variables
    INF = float('inf')
    dist = defaultdict(lambda: INF)    
    dist[src] = 0
    prev = defaultdict(list) # prev holds paths

    # priority queue to hold (node, distance)
    pq = [(0, src)]

    # process until empty
    edges_explored = 0
    while pq:
        distance, node = heapq.heappop(pq)
        if distance > dist[node]:
            continue
        
        # Break early once we reach the end node
        if node == to:
            break
        
        # relax all of node's edges
        for v in graph.get_neighbors(node):
            edges_explored += 1
            
            weight = 1 # unweighted so all edges w=1
            
            # node allows a smaller weight
            if dist[v] > distance + weight:
                # replace the weight, append to pq
                dist[v] = distance + weight
                prev[v] = [node]
                heapq.heappush(pq, (dist[v], v))
            elif dist[v] == distance + weight:
                prev[v].append(node) 

    least_dist = dist[to] if dist[to] < INF else None
    if least_dist is None:
        return edges_explored, None, []

    # now backtrack all the nodes for all shortest paths
    paths = []
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

    return edges_explored, least_dist, paths


# BFS Algorithm - Victoria
def bfs(graph: Graph, src, to):
    if to == src:
        return 0, 0, [[src]]

    # to keep track of nodes visited
    visited = set()
    
    # BFS queue intialized (node, path)
    queue = deque()
    queue.append((src, [src]))
    paths = []

    distance = 0
    edges_explored = 0
    to_visited = False
    while queue:
        size = len(queue)
        
        for _ in range(size):
            # FIFO
            node, path = queue.popleft()
            visited.add(node)

            # checking all neighbors
            for neighbor in graph.get_neighbors(node):
                # Skip already visited nodes
                if neighbor in visited: continue
                
                edges_explored += 1
                
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                if neighbor == to:
                    to_visited = True
                    paths.append(new_path)
        
        distance += 1
        
        # Break early if we reach the end node
        if to_visited:
            break

    # if not reachable
    if not to_visited:
        return edges_explored, None, []
    return edges_explored, distance, paths