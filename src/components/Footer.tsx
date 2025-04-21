import "../styles/Footer.css";

export default function Footer() {
  return (
    <div id="footer-container">
      <div id="general-stats">
        <h3>Did you know?</h3>
        <p>The longest path is between <b>Interbase</b> and <b>Timken 1111</b> with <i><b>9 degrees</b></i> of separation!</p>
      </div>

      <div id="footer">
        <span id="footer-credits">
          Made by Steve Sajeev, Sriram Yerramsetty, and Victoria Villasana for COP3530 at the University of Florida.
        </span>
        <div id="footer-info">
          <span id="footer-info-left">
            4,592 articles &amp; 119,882 links
          </span>
          <span>&nbsp;&bull;&nbsp;</span>
          <a href="https://snap.stanford.edu/data/wikispeedia.html">Dataset</a>
        </div>
      </div>
    </div>
  );
}