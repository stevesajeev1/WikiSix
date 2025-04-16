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
      <button id="find-connection-btn">Find Connection</button>
      <div id="general-stats">
        <h3>General Statistics</h3>
        <p>The longest path in this dataset is <b>x to y</b>:</p>
        <p><b>x</b> → z → c → a → j → l → y → <b>y</b></p>
        <p>Another stat...</p>
      </div>
    </div>
  );
}