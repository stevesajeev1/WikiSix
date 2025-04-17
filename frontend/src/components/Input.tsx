import "../styles/Input.css";

export default function Input() {
  return (
    <div id="input-container">
      <span>Find the shortest paths from</span>
      <div id="inputs">
        <input />
        <span>to</span>
        <input />
      </div>
      <div id="input-button">Go!</div>
    </div>
  );
}