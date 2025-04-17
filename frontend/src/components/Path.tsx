import "../styles/Path.css";

interface PathProps {
  path: string[];
}

export default function Path({ path }: PathProps) {
  return (
    <div id="path-parts">
      {path.map((part, i) => 
        <div
          key={i}
          className="path-part"
          style={{ borderLeft: `15px solid hsl(${i * (360 / path.length)}, 80%, 65%)` }}
        >
          {part}
        </div>
      )}
    </div>
  );
}