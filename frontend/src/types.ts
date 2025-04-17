type Algorithm = {
  time: number,
  edges_explored: number
}

export type User = {
  average_length: number,
  average_duration: number,
  shortest_path: string[],
  shortest_degree: number
}

export type Result = {
  shortest_degree: number,
  paths: string[][],
  dijkstra: Algorithm,
  dfs: Algorithm,
  bfs: Algorithm,
  user: User
};