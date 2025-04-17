import "../styles/Graph.css";

import type { Result } from '../types';
import { GraphCanvas } from 'reagraph';

interface GraphProps {
  result: Result;
}

export default function Graph({ result }: GraphProps) {
  return (
    <div id="graph-container">
      <div id="canvas-container">
        <GraphCanvas
          nodes={[
            {
              id: 'n-1',
              label: '1'
            },
            {
              id: 'n-2',
              label: '2'
            }
          ]}
          edges={[
            {
              id: '1->2',
              source: 'n-1',
              target: 'n-2',
              label: 'Edge 1-2'
            }
          ]}
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
            <tr>
              <td>BFS</td>
              <td>{result.bfs.edges_explored}</td>
              <td>{result.bfs.time}</td>
            </tr> */}
          </tbody>
        </table>
      </div>
      <span id="graph-description">Found {result.paths.length} paths with {result.shortest_degree} degrees of separation!</span>
    </div>
  );
}