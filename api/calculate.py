import time
import json
from .graph import Graph
from .algorithms import dijkstra, bfs
from .user_route import get_user_route

from http.server import BaseHTTPRequestHandler

# We will have a global variable storing the graph.
# We do not want to create a new graph on each request.
graph = Graph("./data/paths.tsv")

# We will have a route that will call all algorithms
class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            self.send_error(400, "Please supply a start and end node!")
            return

        try:
            body = self.rfile.read(content_length)
            data = json.loads(body)
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON format!")
            return
        
        if 'start' not in data or not data['start'] or 'end' not in data or not data['end']:
            self.send_error(400, "Please supply a start and end node!")
            return

        # get nodes from request
        start = data['start'].lower().replace(' ', '_')
        end = data['end'].lower().replace(' ', '_')

        # make sure start and end nodes in graph
        if not graph.hasNode(start):
            self.send_error(400, f"{start} not in dataset!")
            return
        if not graph.hasNode(end):
            self.send_error(400, f"{end} not in dataset!")
            return

        # Run the algorithms and record time taken where:
            # time_alg - time taken
            # ee_alg - number of edges explored
            # dg_alg - lowest degree of seperation
            # paths_alg - paths returned

        time_djk, ee_djk, dg_djk, paths_djk = time_function(dijkstra, start, end)
        time_bfs, ee_bfs, dg_bfs, paths_bfs  = time_function(bfs, start, end)

        # Check if paths are equal
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
    self.send_response(200)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(result).encode('utf-8'))


# Function to time each algorithm
def time_function(function, start, end):
    # consider creating a thread as well
    st = time.perf_counter()
    ee, dg, paths = function(graph, start, end)
    et = time.perf_counter()
    time_taken = et - st
    return time_taken, ee, dg, paths