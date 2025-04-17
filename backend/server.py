from flask import Flask, request, jsonify
from flask_cors import CORS
from graph import Graph
import algorithms
import time
import user_route

app = Flask(__name__)
CORS(app)

# We will have a global variable storing the graph.
# We do not want to create a new graph on each request.
graph = Graph("./data/paths.tsv")

# We will have a route that will call all algorithms
@app.route("/calculate", methods=['POST'])
def calculate():
    if request.json is None or 'start' not in request.json or 'end' not in request.json:
        return 'Please supply a start and end node', 400
    
    # get nodes from request
    start = (request.json['start']).lower().replace(' ', '_')
    end = (request.json['end']).lower().replace(' ', '_')

    # make sure start and end nodes in graph
    if not graph.hasNode(start): return "Start node not in graph", 400
    if not graph.hasNode(end): return "End node not in graph", 400

    # Run the algorithms and record time taken where:
        # time_alg - time taken
        # ee_alg - number of edges explored
        # dg_alg - lowest degree of seperation
        # paths_alg - paths returned
    
    time_djk, ee_djk, dg_djk, paths_djk = time_function(algorithms.dijkstra, start, end)
    # time_dfs, ee_dfs, dg_dfs, paths_dfs = time_function(algorithms.dfs, start, end)
    time_bfs, ee_bfs, dg_bfs, paths_bfs  = time_function(algorithms.bfs, start, end)
    
    # Check if paths are equal
    # if (dg_bfs != dg_dfs != dg_djk) or (len(paths_bfs) != len(paths_dfs) != len(paths_djk)):
            # return "Error, paths returned not equal", 500
    
    # finding user routes
    avg_user_path_len, avg_user_duration, shortest_user_path = user_route.get_user_route(start, end)

    result = {
        "shortest_degree": int(dg_djk),
        "paths": paths_djk,
        "dijkstra": {
            "time": time_djk,
            "edges_explored": ee_djk
        },
        # "dfs": {
        #     "time": time_dfs,
        #     "edges_explored": ee_dfs
        # },
        "bfs": {
            "time": time_bfs,
            "edges_explored": ee_bfs
        },
        "user": {
            "average_length": avg_user_path_len,
            "average_duration": avg_user_duration,
            "shortest_path": shortest_user_path,
            "shortest_degree": 0 if (shortest_user_path is None) else len(shortest_user_path)
        }
    }

    # Return the times, edges explored (for each), and a single paths (list of lists)
    return jsonify(result)


# Function to time each algorithm
def time_function(function, start, end):
    # consider creating a thread as well
    st = time.perf_counter()
    ee, dg, paths = function(graph, start, end)
    et = time.perf_counter()
    time_taken = et - st
    return time_taken, ee, dg, paths