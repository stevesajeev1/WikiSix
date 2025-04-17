from flask import Flask, request, jsonify
from flask_cors import CORS
from graph import Graph
import algorithms
import time

app = Flask(__name__)
CORS(app)

# We will have a global variable storing the graph.
# We do not want to create a new graph on each request.
graph = Graph("backend/data/paths.tsv")

@app.route("/")
def hello_world():
    return "Hello, world!"

# We will have a route that will call all algorithms
# TODO: Should this be parallelized?
@app.route("/calculate", methods=['POST'])
def calculate():
    if request.json is None or 'start' not in request.json or 'end' not in request.json:
        return 'Please supply a start and end node', 400
    
    # get nodes from request
    start = (request.json['start']).lower()
    end = (request.json['end']).lower()

    # make sure start and end nodes in graph
    if not graph.hasNode(start): return "Start node not in graph"
    if not graph.hasNode(end): return "End node not in graph"

    # Run the algorithms and record time taken where:
        # time_alg - time taken
        # ne_alg - number of edges explored
        # dg_alg - lowest degree of seperation
        # paths_alg - paths returned
    
    time_djk, ne_djk, dg_djk, paths_djk = time_function(algorithms.dijkstra, graph, start, end)
    time_dfs, ne_dfs, dg_dfs, paths_dfs = time_function(algorithms.dfs, graph, start, end)
    time_bfs, ne_bfs, dg_bfs, paths_bfs  = time_function(algorithms.bfs, graph, start, end)
    
    # Check if paths are equal
    if (dg_bfs != dg_dfs != dg_djk) or (len(paths_bfs) != len(paths_dfs) != len(paths_djk)):
            return "Error, paths returned not equal", 500

    result = {
        "shortest_degree": int(dg_djk),
        "paths": paths_djk,
        "dijkstra": {
            "time": time_djk,
            "edges_explored": ne_djk
        },
        "dfs": {
            "time": time_dfs,
            "edges_explored": ne_dfs
        },
        "bfs": {
            "time": time_bfs,
            "edges_explored": ne_bfs
        }
    }

    # Return the times, edges explored (for each), and a single paths (list of lists)
    return jsonify(result)


# Function to time each algorithm
def time_function(function, graph, start, end):
    # consider creating a thread as well
    st = time.perf_counter()
    ne, dg, paths = function(graph, start, end)
    et = time.perf_counter()
    time_taken = et - st
    return time_taken, ne, dg, paths