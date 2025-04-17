import type { User } from "../types";

interface UserProps {
  user: User;
}

export default function UserPaths({ user }: UserProps) {
  return <span>User Paths</span>;
}