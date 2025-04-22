from flask import Flask, request, jsonify
from flask_cors import CORS
import time
from .graph import Graph
from .algorithms import dijkstra, bfs
from .user_route import get_user_route

app = Flask(__name__)
CORS(app)

# We will have a global variable storing the graph.
# We do not want to create a new graph on each request.
graph = Graph("./data/paths.tsv")

# We will have a route that will call all algorithms
@app.route("/api/calculate", methods=['POST'])
def calculate():
    print("called")
    if request.json is None or 'start' not in request.json or 'end' not in request.json:
        return 'Please supply a start and end node', 400
    
    # get nodes from request
    start = (request.json['start']).lower().replace(' ', '_')
    end = (request.json['end']).lower().replace(' ', '_')

    # make sure start and end nodes in graph
    if not graph.hasNode(start): return f"{start} not in dataset!", 400
    if not graph.hasNode(end): return f"{end} not in dataset!", 400

    # Run the algorithms and record time taken where:
        # time_alg - time taken
        # ee_alg - number of edges explored
        # dg_alg - lowest degree of seperation
        # paths_alg - paths returned
    
    time_djk, ee_djk, dg_djk, paths_djk = time_function(dijkstra, start, end)
    time_bfs, ee_bfs, dg_bfs, paths_bfs  = time_function(bfs, start, end)
    
    if (dg_bfs != dg_djk) or (len(paths_bfs) != len(paths_djk)):
            return "Error, paths returned not equal", 500
    
    # finding user routes
    avg_user_path_len, avg_user_duration, shortest_user_path = get_user_route(start, end)

    result = {
        "shortest_degree": int(dg_djk),
        "paths": paths_djk,
        "dijkstra": {
            "time": round(time_djk, 4),
            "edges_explored": ee_djk
        },
        "bfs": {
            "time": round(time_bfs, 4),
            "edges_explored": ee_bfs
        },
        "user": None if shortest_user_path is None else {
            "average_length": avg_user_path_len,
            "average_duration": avg_user_duration,
            "shortest_path": shortest_user_path,
            "shortest_degree": len(shortest_user_path)
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