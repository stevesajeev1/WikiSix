import "../styles/Paths.css";

import Path from "./Path";

interface PathsProps {
  paths: string[][];
}

export default function Paths({ paths }: PathsProps) {
  return (
    <div id="paths-container">
      <span>Individual Paths</span>
      {paths.map((path, i) => 
        <Path key={i} path={path} />
      )}
    </div>
  )
}