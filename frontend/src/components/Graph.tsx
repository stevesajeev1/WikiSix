import "../styles/Graph.css";

import type { Result } from '../types';
import { GraphCanvas, GraphNode, GraphEdge } from 'reagraph';

interface GraphProps {
  result: Result;
}

export default function Graph({ result }: GraphProps) {
  const nodes: GraphNode[] = [];
  const edges: GraphEdge[] = [];

  // ADDING EDGEs AND NODES
  result.paths.forEach((path) => {
    for (let i = 0; i < path.length; i++){
      if (!nodes.some((node) => node.id === path[i])) {
        let degrees = i * (360 / path.length);
        let color = `hsl(${degrees}, 80%, 65%)`;
        nodes.push({ id: path[i], label: path[i], fill: color });
      }      
      if (i < path.length - 1) {
        if (!edges.some((edge) => edge.id === `${path[i]}->${path[i + 1]}`))
        edges.push({ // adding the edges b/w consecutive nodes in the list
          id: `${path[i]}->${path[i + 1]}`,
          source: path[i],
          target: path[i + 1],
          label: `${path[i]} -> ${path[i + 1]}`,
        });
      }
    }
  })

  // fullscreen function, on user clicking canvas
  const fullscreenToggle = () => {
    const graphContainer = document.getElementById("graph-container")!;
    if (!document.fullscreenElement) {
      graphContainer.requestFullscreen();
    } else {
      document.exitFullscreen();
    }
  };

  return (
    <div id="graph-container">
      <div id="canvas-container">
      <GraphCanvas
          // create the canvas (graph attributes)
          nodes = {nodes}
          edges= {edges}
          layoutType="treeLr2d" 
          animated={true} 
          edgeArrowPosition="end" 
          draggable={true}
          onCanvasClick = {fullscreenToggle}
          
        />
      </div>
      <div id="stats">
        <h3>Statistics</h3>
        <table>
          <thead>
            <tr>
              <th>Algorithm</th>
              <th>Edges Explored</th>
              <th>Time Taken (s)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Dijkstra</td>
              <td>{result.dijkstra.edges_explored}</td>
              <td>{result.dijkstra.time}</td>
            </tr>
            {/* <tr>
              <td>DFS</td>
              <td>{result.dfs.edges_explored}</td>
              <td>{result.dfs.time}</td>
            </tr>
            */}
            <tr>
              <td>BFS</td>
              <td>{result.bfs.edges_explored}</td>
              <td>{result.bfs.time}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div id="fullscreen-txt">Click Canvas to Enter Fullscreen</div>
      <span id="graph-description">Found {result.paths.length} paths with {result.shortest_degree} degrees of separation!</span>
    </div>
  );
}