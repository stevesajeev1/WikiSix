from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# We will have a global variable storing the graph.
# We do not want to create a new graph on each request.
# graph = Graph(filename)

@app.route("/")
def hello_world():
    return "Hello, world!"

# We will have a route that will call all algorithms
# TODO: Should this be parallelized?
# @app.route("/calculate")
# def calculate(start, end):
#     dijkstra(graph, start, end)
#     dfs(graph, start, end)
#     ...
#     return results