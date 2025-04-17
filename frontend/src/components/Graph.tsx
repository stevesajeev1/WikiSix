import "../styles/Graph.css";

import { GraphCanvas } from 'reagraph';

export default function Graph() {
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
              <th>Time Taken</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Dijkstra</td>
              <td>1000</td>
              <td>1.4s</td>
            </tr>
          </tbody>
        </table>
      </div>
      <span id="graph-description">Found 119 paths with 3 degrees of separation from Google to Krakatoa in 3.38 seconds!</span>
    </div>
  );
}