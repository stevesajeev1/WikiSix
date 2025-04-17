type Algorithm = {
  time: number,
  edges_explored: number
}

export type Result = {
  shortest_degree: number,
  paths: string[][],
  dijkstra: Algorithm
  dfs: Algorithm
  bfs: Algorithm
  user: {
    average_length: number,
    average_duration: number,
    shortest_path: string[],
    shortest_degree: number
  }
};