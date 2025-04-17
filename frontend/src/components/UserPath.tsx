import '../styles/UserPath.css';

import type { User } from "../types";

import Path from './Path';

interface UserProps {
  user: User;
}

export default function UserPaths({ user }: UserProps) {
  return (
    <div id="user-container">
      <span id="user-title">User Path</span>
      <Path path={user.shortest_path} />
      <div id="user-stats">
        <span>The average user took <strong>{user.average_duration}</strong>s to solve.</span>
        <span>The average degree that a user found was <strong>{user.average_length}</strong>.</span>
        <span>The shortest degree that a user found was <strong>{user.shortest_degree}</strong>.</span>
      </div>
    </div>
  )
}